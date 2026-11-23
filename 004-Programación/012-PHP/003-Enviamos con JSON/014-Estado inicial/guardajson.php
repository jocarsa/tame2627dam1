<?php
// API de pedidos: JSON por POST, con respuesta JSON.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
function responder(int $estado, array $datos): void {
    http_response_code($estado);
    echo json_encode($datos, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') responder(405, ['ok'=>false, 'error'=>'Utiliza POST']);
$entrada = file_get_contents('php://input');
if ($entrada === false || strlen($entrada) > 1000000) responder(413, ['ok'=>false, 'error'=>'Pedido demasiado grande']);
$pedido = json_decode($entrada, true);
if (!is_array($pedido)) responder(400, ['ok'=>false, 'error'=>'JSON inválido']);
$nombre = trim((string)($pedido['nombre'] ?? ''));
$email = trim((string)($pedido['email'] ?? ''));
$productos = $pedido['productos'] ?? null;
if ($nombre === '' || strlen($nombre) > 150 || !filter_var($email, FILTER_VALIDATE_EMAIL) || strlen($email) > 254) {
    responder(422, ['ok'=>false, 'error'=>'Nombre o correo electrónico no válido']);
}
if (!is_array($productos) || count($productos) === 0 || count($productos) > 200) {
    responder(422, ['ok'=>false, 'error'=>'El pedido debe contener productos']);
}
// Consultamos precios reales en SQLite; nunca confiamos en el total enviado por el navegador.
try {
    $db = new SQLite3(__DIR__ . '/tienda.db', SQLITE3_OPEN_READONLY);
    $consulta = $db->prepare('SELECT nombre, precio FROM productos WHERE nombre = :nombre LIMIT 1');
    $lineas = [];
    $totalCentimos = 0;
    foreach ($productos as $item) {
        if (!is_array($item) || !is_string($item['producto'] ?? null)) responder(422, ['ok'=>false, 'error'=>'Producto no válido']);
        $consulta->bindValue(':nombre', $item['producto'], SQLITE3_TEXT);
        $resultado = $consulta->execute();
        $producto = $resultado->fetchArray(SQLITE3_ASSOC);
        $resultado->finalize();
        if (!$producto) responder(422, ['ok'=>false, 'error'=>'Producto no encontrado']);
        $centimos = (int)round((float)$producto['precio'] * 100);
        if ($centimos < 0) responder(422, ['ok'=>false, 'error'=>'Precio no válido']);
        $totalCentimos += $centimos;
        $lineas[] = ['producto'=>$producto['nombre'], 'precio'=>$centimos / 100];
    }
    $db->close();
} catch (Throwable $e) {
    responder(500, ['ok'=>false, 'error'=>'No se pudo consultar el catálogo']);
}
try {
    $id = date('Ymd_His') . '_' . bin2hex(random_bytes(6));
    $registro = [
        'id'=>$id,
        'fecha'=>date('c'),
        'fecha_cliente'=>is_string($pedido['fecha'] ?? null) ? substr($pedido['fecha'], 0, 40) : null,
        'nombre'=>$nombre,
        'email'=>$email,
        'productos'=>$lineas,
        'total'=>$totalCentimos / 100
    ];
    $directorio = __DIR__ . '/json';
    if (!is_dir($directorio) && !mkdir($directorio, 0750, true) && !is_dir($directorio)) throw new RuntimeException('No se puede crear la carpeta');
    $ruta = $directorio . '/' . $id . '.json';
    $contenido = json_encode($registro, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR);
    $archivo = fopen($ruta, 'x');
    if (!$archivo) throw new RuntimeException('No se puede crear el pedido');
    $escrito = fwrite($archivo, $contenido);
    fclose($archivo);
    if ($escrito !== strlen($contenido)) { unlink($ruta); throw new RuntimeException('Escritura incompleta'); }
    responder(201, ['ok'=>true, 'id'=>$id, 'fecha'=>$registro['fecha']]);
} catch (Throwable $e) {
    responder(500, ['ok'=>false, 'error'=>'No se pudo guardar el pedido']);
}

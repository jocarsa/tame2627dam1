<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      html,body{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;justify-content:center;align-items:center;background:indigo;}
      form{width:300px;height:300px;padding:20px;background:white;display:flex;flex-direction:column;gap:20px;justify-content:center;}
      input{padding:10px;}
    </style>
  </head>
  <body>
    <form method="POST" action="validame.php">
    	
      <input type="text" name="usuario" placeholder="usuario">
      <input type="password" name="contrasena" placeholder="contraseña">
      <input type="submit">
    </form>
  </body>
</html>
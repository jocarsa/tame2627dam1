package proyecto008clases;

public class Proyecto008Clases {
 
    public static void main(String[] args) {
        // En la instanciación hay que indicar el tipo de dato
        // Cliente es el tipo de datos del objeto
        // Cliente1 es el nombre de la instancia que creo (aqui podeis poner lo que querais)
        // new es la palabra reservada que usamos para instanciar
        // Cliente es la llamada a la clase (que lleva parametros de constructor)
        Cliente Cliente1 = new Cliente("Jose Vicente","Carratala",48);
        System.out.println(Cliente1.edad);
        System.out.println(Cliente1.dameEdad());
    }
    
}

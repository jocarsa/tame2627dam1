package proyecto008clases;

public class Cliente {
    String nombre;
    String apellidos;
    int edad;
    
    public Cliente(String nuevo_nombre,String nuevos_apellidos,int nueva_edad){
        nombre = nuevo_nombre;
        apellidos = nuevos_apellidos;
        edad = nueva_edad;
    }
    public String dameNombre(){
        return nombre+apellidos;
    }
    public int dameEdad(){
        return edad;
    }
}

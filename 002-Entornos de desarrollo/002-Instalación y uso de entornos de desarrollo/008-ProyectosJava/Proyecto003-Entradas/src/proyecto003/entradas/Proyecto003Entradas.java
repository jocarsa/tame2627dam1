package proyecto003.entradas;

import java.util.Scanner;

public class Proyecto003Entradas {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Introduce tu nombre: ");
        String nombre = entrada.nextLine();
        
        System.out.println("Mi nombre es: "+nombre);
    }
    
}

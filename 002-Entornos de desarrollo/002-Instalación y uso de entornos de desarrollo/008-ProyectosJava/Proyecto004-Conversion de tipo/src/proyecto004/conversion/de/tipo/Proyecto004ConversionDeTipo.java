package proyecto004.conversion.de.tipo;
import static java.lang.Integer.parseInt;
import java.util.Scanner;

public class Proyecto004ConversionDeTipo {

   
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Introduce tu edad: ");
        String edad = entrada.nextLine();
        
        int edad_numero = parseInt(edad);
        int doble = edad_numero*2;
        
        System.out.println("El doble de tu edad es de "+doble+" años");
        
    }
    
}

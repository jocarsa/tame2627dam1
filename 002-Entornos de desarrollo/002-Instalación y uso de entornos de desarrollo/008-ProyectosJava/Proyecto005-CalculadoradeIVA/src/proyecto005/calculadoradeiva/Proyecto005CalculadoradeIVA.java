/*
    Programa calculadora de IVA
    v0.1
    Jose Vicente Carratala
*/

package proyecto005.calculadoradeiva;
import static java.lang.Integer.parseInt;
import java.util.Scanner;

public class Proyecto005CalculadoradeIVA {

    public static void main(String[] args) {
        // Primero entrada de datos
        Scanner entrada = new Scanner(System.in);
        System.out.print("Introduce la base imponible: ");
        String base = entrada.nextLine();
        
        System.out.print("Introduce el porcentaje de IVA: ");
        String porcentaje = entrada.nextLine();
        
        // Ahora conversiones de tipo
        
        int base_numero = parseInt(base);
        int porcentaje_numero = parseInt(porcentaje);
        
        // Luego cálculos
        
        double iva = base_numero*(porcentaje_numero/100.0);
        double total = base_numero+iva;
        
        // Por ultimo resultados
        
        System.out.println("Tu base es de: "+base_numero);
        System.out.println("El IVA es de: "+iva);
        System.out.println("El total de la factura es de: "+total);
    }
    
}

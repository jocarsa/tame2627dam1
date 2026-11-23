/*
	Programa calculadora de IVA
  v0.1 por Jose Vicente Carratala
*/
#include <stdio.h>

int main(){
		// Primero declaro variables
    int base;
    float iva;
    float total;
    
    // Ahora el usuario introduce datos
    printf("Introduce una base: ");
    scanf("%d", &base);
    
    // Ahora realizo cálculos
    iva = base*0.21;
    total = base + iva;
    
    // Y por último muestro resultados
    printf("La base de cálculo es: %d\n", base);
    printf("El total del IVA es: %f\n", iva);
    printf("El total de la factura es: %f\n", total);
    return 0;
}
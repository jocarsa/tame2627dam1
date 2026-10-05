/*
	Programa calculadora de IVA
  v0.1 por Jose Vicente Carrataña
*/
#include <stdio.h>

int main(){
    int base;
    printf("Introduce una base: ");
    scanf("%d", &base);
    float iva;
    iva = base*0.21;
    float total = base + iva;
    printf("La base de cálculo es: %d\n", base);
    printf("El total del IVA es: %f\n", iva);
    printf("El total de la factura es: %f\n", total);
    return 0;
}
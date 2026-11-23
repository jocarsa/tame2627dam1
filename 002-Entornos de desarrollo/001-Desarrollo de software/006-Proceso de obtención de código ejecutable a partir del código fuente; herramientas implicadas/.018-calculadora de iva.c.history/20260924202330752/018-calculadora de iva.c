#include <stdio.h>

int main(){
    int base;
    printf("Introduce una base: ");
    scanf("%d", &base);
    float iva;
    iva = base*0.21;
    printf("El base de cálculo es:: %d\n", base);
    return 0;
}
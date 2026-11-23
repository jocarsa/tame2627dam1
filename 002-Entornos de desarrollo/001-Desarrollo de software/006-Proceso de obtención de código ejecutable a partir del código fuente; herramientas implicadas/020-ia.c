/*
    Programa calculadora de IVA
    v0.2 por Jose Vicente Carratala
*/

#include <stdio.h>

int main(){

    // ================================
    // DECLARACIÓN DE VARIABLES
    // ================================

    float base;
    float iva;
    float total;

    // ================================
    // LIMPIAMOS LA PANTALLA
    // ================================

    printf("\033[2J");

    // Colocamos el cursor arriba a la izquierda
    printf("\033[1;1H");


    // ================================
    // CABECERA
    // ================================

    // Fondo azul + texto blanco + negrita
    printf("\033[44;97;1m");
    printf("                                                    \n");
    printf("              CALCULADORA DE IVA v0.2              \n");
    printf("              Jose Vicente Carratala               \n");
    printf("                                                    \n");
    printf("\033[0m");


    // ================================
    // ENTRADA DE DATOS
    // ================================

    printf("\n");

    printf("\033[1;36m");
    printf("+--------------------------------------------------+\n");
    printf("|               ENTRADA DE DATOS                   |\n");
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");

    printf("\n");

    printf("  Introduce la base imponible: ");

    // Color amarillo para lo que escriba el usuario
    printf("\033[1;33m");
    scanf("%f", &base);
    printf("\033[0m");


    // ================================
    // CÁLCULOS
    // ================================

    iva = base * 0.21;
    total = base + iva;


    // ================================
    // RESULTADOS
    // ================================

    printf("\n");

    printf("\033[1;32m");
    printf("+--------------------------------------------------+\n");
    printf("|                    RESULTADO                     |\n");
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");

    printf("|                                                  |\n");

    printf("|  Base imponible:        %10.2f euros        |\n", base);
    printf("|  IVA (21%%):             %10.2f euros        |\n", iva);

    printf("|                                                  |\n");

    printf("\033[1;32m");
    printf("+--------------------------------------------------+\n");
    printf("|  TOTAL:                 %10.2f euros        |\n", total);
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");


    // ================================
    // EXPLICACIÓN DIDÁCTICA
    // ================================

    printf("\n");

    printf("\033[1;35m");
    printf("COMO SE HA CALCULADO\n");
    printf("====================\n");
    printf("\033[0m");

    printf("IVA   = %.2f x 0.21 = %.2f\n", base, iva);
    printf("TOTAL = %.2f + %.2f = %.2f\n", base, iva, total);


    // ================================
    // DESPEDIDA
    // ================================

    printf("\n");
    printf("\033[90m");
    printf("Pulsa ENTER para finalizar...");
    printf("\033[0m");

    getchar();
    getchar();

    return 0;
}
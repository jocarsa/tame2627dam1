#include <stdio.h>

int main(){
	int edad = 48;
  if(edad < 10){
  	printf("eres un niño \n");
  }else if(edad >= 10 && edad < 20){
  	printf("eres un adolescente \n");
  }else if(edad >= 20 && edad < 30){
  	printf("eres un joven \n");
  }else if(edad >= 30 && edad < 40){
  	printf("eres un adulto \n");
  }else{
  	printf("eres ya muy mayor \n");
  }
  
  return 0;
}
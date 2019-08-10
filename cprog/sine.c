#include <stdio.h>
#include <math.h>
#define PI 3.141592

int main() {
  int i,j=0;
  double y,x=0;
  int line=0;

  for(i=0;i<500;i++){
    x=x+PI/45;
    y=50*sin(x)+50;
    for(j=0; j<= round(y); j++){
      printf(" ");
    } 
    if (line==0) {
	printf("hello\n");
	line=1;
    }
    else {
	printf("math world\n");
	line=0;
    }
  }
return 0;
}



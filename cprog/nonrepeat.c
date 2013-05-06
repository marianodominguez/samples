#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int indexOf(char a, char *s) {
    int i=0;
    while(i<strlen(s)) {
        if(a == s[i]) return i;
        i++;
    }
    return -1;
}

int ocurrencesOf(char a, char *s) {
    int result =0;
    int i=0;
    for(i=0;i<strlen(s);i++) {
        if(a == s[i]) result++;
    }
    return result;
}

char findNonRepeating(char *s) {
    int i=0;
	for(i=0; i<strlen(s); i++) {
	    if ( ocurrencesOf(s[i], s) == 1 ) return s[i];
	}
	return 0;
}

int main(int argc, char *argv[] ) {
      if (argc <= 1) {
        printf("not enough arguments\n");
        exit(1);
      };
      char* s = argv[1];
      printf("%s\n",s);
      //printf("%d\n",indexOf('b',"acdb"));  
      printf("%c\n",findNonRepeating(s));
return 0;
}

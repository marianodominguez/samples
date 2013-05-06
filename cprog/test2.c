#include <stdio.h>

void foo(void)
{
	int a=3;
	++a;
	printf("%d\n", a);
}

int main(void)
{
	foo();
	foo();
	foo();
}


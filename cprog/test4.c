#include <stdio.h>

void foo(void)
{
    int a;
    ++a;
    printf("%d\n", a);
}

int main(void)
{
    foo();
    foo();
    foo();
}


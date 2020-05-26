#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

typedef unsigned long u64;

static u64 get_rcx() {
    __asm__ __volatile__(
            "mov r0, #10\n\t" 
            "bx lr"); 
            /* at&t syntax: movq <src_reg>, <dest_reg> */  
    }


int main(void)
{
    printf("get value from asm: [RCX] = 0x%lx\n", get_rcx());
    exit(0);
}
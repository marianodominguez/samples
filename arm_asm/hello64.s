.section .data
msg: .ascii "Hello, World!\n"
len = . - msg

.section .text
.global _start
_start:
    //write(1, msg, len)
    mov x0, #1
    ldr x1, =msg
    mov x2, #len
    mov x8, #64
    svc #0

    //Exit the program
    mov x0, #0
    mov x8, #93
    svc #0

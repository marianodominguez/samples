.data
msg: .ascii "Hello, World!\n"
len: . - msg
.text
.global _start
_start:

    mov r0, #1
    ldr r1, =msg
    mov r2, len
    mov r8, #64
    svc 0

    @ Exit the program
    mov r0, #0
    mov r7, #93
    svc 0

.data
msg: .ascii "Hello, World!\n"
len = . - msg
.text
.global _start
_start:
    mov r0, #1
    mov r2, #len
    ldr r1, =msg
    mov r7, #4
    svc 0

    @ Exit the program
    mov r0, #0
    mov r7, #1
    svc 0

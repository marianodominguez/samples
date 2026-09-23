.section .data
msg: .ascii "0\n"
len = . - msg

.section .text
.global _start
_start:
    mov w10, #0 // Initialize counter to 0
    ldr x1, =msg
loop:
    cmp w10, #9 // Compare counter with 9
    beq exit // If counter == 9, exit the loop
    
    add w10, w10, #1 // Increment counter
    ldrb w11, [x1] // Load the current character from msg
    add w11, w11, #1 // Increment the character (ASCII value)
    strb w11, [x1] // Store the incremented character back in msg

    //write(1, msg, len)
    mov x0, #1
    mov x2, #len
    mov x8, #64
    svc #0
    b loop // Repeat the loop 

    //Exit the program
exit:
    mov x0, #0
    mov x8, #93
    svc #0

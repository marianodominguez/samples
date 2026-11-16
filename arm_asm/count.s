.section .data
msg: .ascii "0\n"
len = . - msg

.section .text
.global _start
_start:
    mov r10, #0 // Initialize counter to 0
    ldr r1, =msg
loop:
    cmp r10, #9 // Compare counter with 9
    beq exit // If counter == 9, exit the loop
    
    add r10, r10, #1 // Increment counter
    ldrb r11, [r1] // Load the current character from msg
    add r11, r11, #1 // Increment the character (ASCII value)
    strb r11, [r1] // Store the incremented character back in msg

    //write(1, msg, len)
    mov r0, #1
    mov r2, #len
    mov r7, #4
    svc #0
    b loop // Repeat the loop 

    //Exit the program
exit:
    mov r0, #0
    mov r7, #1
    svc #0

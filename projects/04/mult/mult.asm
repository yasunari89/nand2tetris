// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

    @counter
    M=0
    @2
    M=0
(LOOP)
    @counter
    M=M+1 // counter = counter + 1
    @counter
    D=M // D = counter
    @0
    D=D-M // D = D - R0
    @END
    D;JGT // if counter - R0 > 0: break
    @1
    D=M // D = R1
    @2
    M=D+M // R2 = R1 + R2
    @LOOP
    0;JMP
(END)
    @END
    0;JMP

// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
    @8192
    D = A 
    @SCREEN_SIZE
    M = D
    @16384
    D = A
    @FIRST_PIXEL
    M = D
    @BLACK 
    M = -1
    @WHITE 
    M = 0
    @24576
    D = M 
    @BLACK_LOOP
    D; JNE
    @WHITE_LOOP
    D; JEQ


    (BLACK_LOOP)
        @BLACK
        D = M
        @FIRST_PIXEL
        A = M 
        M = D
        @FIRST_PIXEL
        M = M + 1
        @SCREEN_SIZE
        M = M - 1
        @SCREEN_SIZE
        D = M
        @LOOP
        D; JEQ
        @24576
        D = M
        @LOOP 
        D; JEQ
        @BLACK_LOOP
        0; JMP

    (WHITE_LOOP)
        @WHITE
        D = M
        @FIRST_PIXEL
        A = M 
        M = D
        @FIRST_PIXEL
        M = M + 1
        @SCREEN_SIZE
        M = M - 1
        @SCREEN_SIZE
        D = M
        @LOOP
        D; JEQ
        @24576
        D = M
        @LOOP 
        D; JNE
        @WHITE_LOOP
        0; JMP
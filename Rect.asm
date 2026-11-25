// Draws a rectangle of height 20
@20
D=A
@R0
M=D
@16384
D=A
@R1
M=D

(LOOP)
@R1
A=M
M=-1
@R1
M=M+1
@R0
MD=M-1
@LOOP
D;JGT

(END)
@END
0;JMP

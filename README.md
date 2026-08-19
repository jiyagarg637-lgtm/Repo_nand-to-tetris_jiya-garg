# Repo_nand-to-tetris_jiya-garg
#Not gate
CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in , b=in, out=out);
}

#And gate
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a , b=b , out=nandOut);
    Not(in=nandOut , out=out);
    
}

#Or gate
CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a , b=b , out=c );
    Nand(a=b , b=b , out=j );
    Nand(a=c , b=j , out=out );
}

#Xor
CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a, b=b, out=n1);
    Nand(a=a, b=n1, out=n2);
    Nand(a=b, b=n1, out=n3);
    Nand(a=n2, b=n3, out=out);
    
}

#Mux
CHIP Mux {
    IN a, b, sel;
    OUT out;

    PARTS:
     Not(in=sel, out=nsel);
    And(a=a, b=nsel, out=x);
    And(a=b, b=sel, out=y);
    Or(a=x, b=y, out=out);
}

#DMux
CHIP DMux {
    IN in, sel;
    OUT a, b;

    PARTS:
    Not(in=sel, out=nsel);
    And(a=in, b=nsel, out=a);
    And(a=in, b=sel, out=b);
}

#Not16
CHIP Not16 {
    IN in[16];
    OUT out[16];

    PARTS:
    Not(in=in[0] , out=out[0]);
    Not(in=in[1] , out=out[1]);
    Not(in=in[2] , out=out[2]);
    Not(in=in[3] , out=out[3]);
    Not(in=in[4] , out=out[4]);
    Not(in=in[5] , out=out[5]);
    Not(in=in[6] , out=out[6]);
    Not(in=in[7] , out=out[7]);
    Not(in=in[8] , out=out[8]);
    Not(in=in[9] , out=out[9]);
    Not(in=in[10] , out=out[10]);
    Not(in=in[11] , out=out[11]);
    Not(in=in[12] , out=out[12]);
    Not(in=in[13] , out=out[13]);
    Not(in=in[14] , out=out[14]);
    Not(in=in[15] , out=out[15]);
    
    
}

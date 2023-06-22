    goto main
    wb 0

a ww 400
b ww 19
c ww 10
d ww 0
e ww 0

main        div x, a
            jz x, linha_jump
            store x, d
linha_jump  mult2 x, d
            add x, a
            add x, b
            sub x, c
            store x, e
            halt
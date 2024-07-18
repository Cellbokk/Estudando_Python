print("Qual e o seu turno M (Matutino) V (Vespertino) N (Noturno)")
turno = str(input("Digite seu turno:")).upper().strip()

if turno == 'M':
    print("Bom dia!!")
elif turno == 'V':
    print("Boa tarde!!")
elif turno == 'N':
    print("Boan noite!!")
else:
    print("Valor invalido!!")

#Problema: SOS morse
#Entrada
mensagem = str(input())
#Detectando sos
if "...---..." in mensagem:
    print("S")
else:
    print("N")
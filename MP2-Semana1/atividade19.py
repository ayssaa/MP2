#Problema: Uma mentira que mata #2
#Entrada
pais1 = str(input())
porcentagem1 = float(input())
pais2 = str(input())
porcentagem2 = float(input())
#Saida
if porcentagem1 > porcentagem2:
    print(pais1, ">" , pais2)
if porcentagem1 < porcentagem2:
    print(pais2, ">" , pais1)
if porcentagem1 == porcentagem2:
    print(pais1, "=" , pais2)
#Problema: Mulheres brasileiras podem votar
#Entrada
ano = int(input())
#Saida
if ano < 1932:
    print("mulheres proibidas de votar")
if ano >= 1932 and ano < 1946:
    print("voto facultativo para mulheres")
if ano >= 1946:
    print("voto obrigatório para mulheres")
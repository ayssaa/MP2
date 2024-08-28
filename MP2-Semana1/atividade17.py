#Problema: Relatório #3
#Entrada
qnt_alunas = int(input())
soma = 0
for i in range(qnt_alunas):
    nota = int(input())
    soma += nota
media = soma / qnt_alunas
#Saida
print("média", "%.1f" % media)
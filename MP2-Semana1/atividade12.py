#Problema: strings, inteiros e floats
#Entrada
opcao = str(input())
#Criando as listas
saida = []
if opcao == "s":
   string = str(input()) 
   for s in string.split():
     saida.append(s)
if opcao == "f":
   inteiro = str(input())
   for i in inteiro.split():
     i = int(i)
     saida.append(i)
if opcao == "n":
   float = str(input())
   for f in float.split():
     f = float()
     saida.append(f)
print(saida)
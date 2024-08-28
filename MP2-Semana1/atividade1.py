#Problema: Variável?
#Entrada
nome = str(input())
auxiliar = ""
digito1 = nome[0].isalpha()
#Verificando o primeiro digito
if nome[0] != "_" and digito1 != True:
    print("ERROR")
#Criando variavel sem _
else:
  for i in nome:
    if i != "_":
      auxiliar = auxiliar + i
#Verificando caracteres invalidos
  if auxiliar.isalnum() == True or auxiliar == "":
    print("OK")
  else:
    print("ERROR")
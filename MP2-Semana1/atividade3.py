#Problema: Cripto weak
#Entrada
trocar = str(input())
substituir = str(input()) 
mensagem = str(input())
#Criptografando
mensagem_cripto = mensagem.replace(trocar,substituir)
#Saida
print(mensagem_cripto)
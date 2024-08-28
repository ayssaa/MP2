#Problema: Uma mentira que mata #1
#Entrada
total_mensagem = int(input())
pais = str(input())
porcentagem_odio = float(input())
odio_mensagem = total_mensagem * porcentagem_odio / 100
#Saida
print("Triste número de mensagens de ódio à população LGBT+ no", pais, "entre 2019 e 2022:")
print("%.0f" % odio_mensagem)
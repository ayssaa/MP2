#Problema: Compra com desconto
#Entrada
produto = float(input())
desconto = float(input())
#Contas
desconto_real = produto * desconto / 100
produto_desconto = produto - desconto_real
#Saida
print("%.2f" % produto)
print("%.2f" % produto_desconto)
print("%.2f" % desconto_real)
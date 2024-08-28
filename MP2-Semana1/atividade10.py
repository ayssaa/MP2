#Problema: A Compra Responsável Informada
#Entrada
valor_banco = int(input())
valor_carrinho = int(input())
#Conta
saldo = valor_banco - valor_carrinho
#Saida
if saldo >= 0:
    print("se você comprar tudo o saldo será:", saldo)
if saldo < 0:
    print("seu saldo é insuficiente para essa compra")    
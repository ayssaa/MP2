#Problema: Balanço financeiro simplificado
#Entrada
movimentacoes = int(input())
balanco = 0
#Saida
for i in range(movimentacoes):
  valor = float(input())
  balanco += valor
print("%.2f" % balanco)
#Problema: Balanço financeiro categorizado
#Entrada
movimentacoes = int(input())
balanco = 0
renda = 0
gasto = 0
S = 0
P = 0
A = 0
M = 0
T = 0
U = 0
L = 0
#Contagem
for i in range(movimentacoes):
  valor = float(input())
  tipo = str(input())
  balanco += valor
  if valor > 0:
    renda += valor
    if tipo == "S":
      S += valor
    if tipo == "P":
      P += valor
  if valor < 0:
    gasto += valor
    if tipo == "A":
      A += valor
    if tipo == "M":
      M += valor
    if tipo == "T":
      T += valor
    if tipo == "S":
      U += valor
    if tipo == "L":
      L += valor
#Saida
print("Movimentações")
if A != 0:
  print("  Alimentação:", "%.2f" % A)
if M != 0:
  print("  Moradia:", "%.2f" % M)
if T != 0:
  print("  Transporte:", "%.2f" % T)
if U != 0:
  print("  Saúde:", "%.2f" % U)
if L != 0:
  print("  Lazer:", "%.2f" % L)
if S != 0:
  print("  Salário:", "%.2f" % S)
if P != 0:
  print("  Prestação de serviços:", "%.2f" % P)
print("Total de Renda:", "%.2f" % renda)
print("Total de Gastos:", "%.2f" % gasto)
print("Balanço:", "%.2f" % balanco)
#Problema: Relatório #2
#Entrada
nome = str(input())
intencao_antes = str(input())
intencao_depois = str(input())
#Saida
if intencao_antes == "S":
    if intencao_depois == "S":
        print(nome, "tinha interesse antes e manteve interesse depois")
    if intencao_depois == "N":
        print(nome, "tinha interesse antes e não manteve interesse depois")
if intencao_antes == "N":
    if intencao_depois == "S":
        print(nome, "não tinha interesse antes e teve interesse depois")
    if intencao_depois == "N":
        print(nome, "não tinha interesse antes e não teve interesse depois")
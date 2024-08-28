#Problema: Trabalheira...
#Entrada
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    check = str(input())
    primeiro += 1
    if check == "ok":
        break
while True:
    check = str(input())
    segundo += 1
    if check == "ok":
        break
while True:
    check = str(input())
    terceiro += 1
    if check == "ok":
        break
while True:
    check = str(input())
    quarto += 1
    if check == "ok":
        break
#Saida
print("Número de versões do primeiro exercício:", primeiro)
print("Número de versões do segundo exercício:", segundo)
print("Número de versões do terceiro exercício:", terceiro)
print("Número de versões do quarto exercício:", quarto)
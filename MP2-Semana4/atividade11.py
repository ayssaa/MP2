# Problema: Poderosas na programação 2
# Entrada: Dado uma lista, achar os 2 menores valores
lista_input = list(map(int, input().split()))


# Definindo minha função que acha o menor valor
def achar_menor(lista):
    if not lista or len(lista) == 1:
        return False
    # Achando o 1° menor
    menor1 = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor1:
            menor1 = lista[i]
    # Achando o 2° menor
    lista.remove(menor1)
    menor2 = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor2:
            menor2 = lista[i]
    return menor1, menor2

# Saida
resposta = achar_menor(lista_input)
if resposta != False:
    print(f'{resposta[0]} {resposta[1]}')
else:
    print('lista pequena demais')
    
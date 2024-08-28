# Problema: Poderosas na programação 1
# Entrada: Dado uma lista, achar o menor valor
lista_input = list(map(int, input().split()))


# Definindo minha função que acha o menor valor
def achar_menor(lista):
    if not lista:
        return 'lista vazia'
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


# Chamando a função
print(achar_menor(lista_input))

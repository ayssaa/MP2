# Problema: Poderosas na Programação 4
# Entrada: Dado uma lista, verificar se ela está em ordem crescente
lista_input = list(map(int, input().split()))


# Definindo minha função que verifica a ordem crescente
def esta_crescente(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return 'N'
    else:
        return 'Y'


# Saida
print(esta_crescente(lista_input))

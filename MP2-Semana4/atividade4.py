# Problema: binary extraction
# Entrada
lista_input = list(map(int, str(input()).split()))
valor_input = int(input())


# Fazendo minha função ordena
def extraction(lista, valor):
    lista_nova = []
    for i in range(valor):
        indice_meio = (len(lista)) // 2
        valor_meio = lista[indice_meio]
        lista_nova.append(valor_meio)
        lista.remove(valor_meio)
    return lista_nova


# Usando a função e Saida
print(lista_input)
print(extraction(lista_input, valor_input))

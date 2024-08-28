# Problema: Quem está no meio?
# Dado uma lista de nomes, colocá-los em ordem alfabética e achar o do meio
# Criando uma lista com os nomes
lista_nomes = []
while True:
    nome_input = str(input())
    if nome_input == '.':
        break
    lista_nomes.append(nome_input)


# Fazendo a lista_ordenada usando a função my_sort()
def my_sort(lista):
    lista_ordenada = []
    for i in range(len(lista)):
        x = min(lista)  # x é o nome mais perto de A
        lista_ordenada.append(x)
        lista.remove(x)
    return lista_ordenada


# Achando o(s) nome(s) do centro
def acha_meio(lista):
    indice_inicial = 0
    indice_final = len(lista) - 1
    indice_meio = (indice_inicial + indice_final) // 2
    if (len(lista) % 2) == 0:
        print(lista[indice_meio])
        print(lista[indice_meio + 1])
    else:
        print(lista[indice_meio])


# Chamando as funções
auxiliar = my_sort(lista_nomes)
acha_meio(auxiliar)

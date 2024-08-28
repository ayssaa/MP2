# Problema: my_pesquisa_binaria()
# Entrada
# Dada uma lista ordenada e um valor procurado, realizar a busca binária mostrando os elementos considerados
lista_ordenada = list(map(int, input().split()))
num_procurado = int(input())


# Definindo minha função my_pesquisa_binaria()
def my_pesquisa_binaria(lista, num):
    indice_inicial = 0
    indice_final = len(lista) - 1
    print(lista)
    while True:
        if indice_inicial > indice_final:
            print("Elemento não encontrado", num)
            break
        if indice_inicial <= indice_final:
            indice_metade = (indice_inicial + indice_final) // 2
            if lista[indice_metade] == num:
                print("Encontrado na posição", indice_metade)
                return indice_metade
            if num < lista[indice_metade]:
                indice_final = indice_metade - 1
                if lista[indice_inicial:indice_final + 1] != []:
                    print(lista[indice_inicial:indice_final + 1])
            if num > lista[indice_metade]:
                indice_inicial = indice_metade + 1
                if lista[indice_inicial:indice_final + 1] != []:
                    print(lista[indice_inicial:indice_final + 1])


# Saida
my_pesquisa_binaria(lista_ordenada, num_procurado)

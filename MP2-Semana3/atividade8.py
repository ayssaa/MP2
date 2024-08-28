# Problema: my_pesquisa_binaria() STRING
# Entrada
# Dada uma lista ordenada e um valor procurado, realizar a busca binária mostrando os elementos considerados
lista_ordenada = list(map(str, input().split()))
str_procurada = str(input())


# Definindo minha função my_pesquisa_binaria()
def my_pesquisa_binaria(lista, string):
    indice_inicial = 0
    indice_final = len(lista) - 1
    print(lista)
    while True:
        if indice_inicial > indice_final:
            print("Elemento não encontrado", string)
            break
        if indice_inicial <= indice_final:
            indice_metade = (indice_inicial + indice_final) // 2
            if lista[indice_metade] == string:
                print("Encontrado na posição", indice_metade)
                return indice_metade
            if string < lista[indice_metade]:
                indice_final = indice_metade - 1
                if lista[indice_inicial:indice_final + 1]:
                    print(lista[indice_inicial:indice_final + 1])
            if string > lista[indice_metade]:
                indice_inicial = indice_metade + 1
                if lista[indice_inicial:indice_final + 1]:
                    print(lista[indice_inicial:indice_final + 1])


# Saida
my_pesquisa_binaria(lista_ordenada, str_procurada)

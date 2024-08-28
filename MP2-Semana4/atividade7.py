# Problema
# Entrada: Uma lista de números inteiros
lista_input = list(map(int, str(input()).split()))
print(lista_input)


# Fazendo minha função
def my_merge_sort(lista):
    print(lista)
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]
        my_merge_sort(esquerda)
        my_merge_sort(direita)
        e = 0
        d = 0
        li = 0
        while e < len(esquerda) and d < len(direita):
            if esquerda[e] < direita[d]:  # se o item E da esquerda for menor que o D da direita:
                lista[li] = esquerda[e]  # item E da esquerda vai para a lista(lista)
                e += 1  # índice E avança em 1
            else:  # caso contrário
                lista[li] = direita[d]    # item D da direita vai para a lista geral (lista_g)
                d += 1  # índice D avança em 1
            li += 1
        while e < len(esquerda):
            lista[li] = esquerda[e]
            e += 1
            li += 1
        while d < len(direita):
            lista[li] = direita[d]
            d += 1
            li += 1


# Saida
my_merge_sort(lista_input)
print(lista_input)

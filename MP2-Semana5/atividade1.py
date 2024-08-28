# Problema:
# Entrada
lista_input = list(map(int, input().split()))
num_input = int(input())
print(lista_input)


# Função recursiva para busca binária
def my_pesquisa_binaria_recursiva(lista, num, indice_inicial, indice_final):
    if indice_inicial <= indice_final:
        metade = (indice_inicial + indice_final) // 2
        print(lista[0:metade])
        if num == lista[metade]:
            return metade
        elif num < lista[metade]:
            return my_pesquisa_binaria_recursiva(lista, num, indice_inicial, metade - 1)
        else:
            return my_pesquisa_binaria_recursiva(lista, num, metade + 1, indice_final)
    else:
        return -1


# Saida
auxiliar = my_pesquisa_binaria_recursiva(lista_input, num_input, 0, len(lista_input) - 1)
if auxiliar == -1:
    print('ausente')
else:
    print(f'posição: {auxiliar}')

# Problema: my_slicing (1)
# Entrada
string = str(input())
indices = [int(i) for i in input().split()]
inicio = indices[0]
fim = indices[1]


# Fazendo a funcao
def my_slicing(inicio, fim):
    contador = -1
    substring = ''
    for i in string:
        contador += 1
        if inicio <= contador < fim:
            substring += i
    return substring


# Saida
print(my_slicing(inicio, fim))

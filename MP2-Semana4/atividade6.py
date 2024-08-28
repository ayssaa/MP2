# Problema: slicing
# Entrada
lista_input = list(map(int, str(input()).split()))
resposta = str(input())


# Fazendo minha função slicing
def slicing(lista):
    indices = list(map(int, str(input()).split()))
    lista_nova = []
    contador = -1
    for elemento in lista:
        contador += 1
        if indices[0] <= contador >= indices[1]:
            lista_nova.append(elemento)
    return lista_nova

# 1 2 3 4 5
# 5

# Fazendo minha função ordena
def ordena(lista):
    lista_nova = []
    for i in range(len(lista)):
        x = lista.pop()
        lista_nova.append(x)
    return lista_nova


# Verificando a resposta
if resposta == 'S':
    print(slicing(lista_input))
elif resposta == 'R':
    print(ordena(lista_input))

# Problema: Nomes das Pontas
# Entrada: Ler nomes de alunas até um '.'
lista_alunas = []
while True:
    aluna = str(input())
    if aluna == '.':
        break
    else:
        lista_alunas.append(aluna)


# Função que ordena listas
def ordena_alpha(lista):
    lista_nova = []
    for numero in range(len(lista)):
        x = min(lista)
        lista_nova.append(x)
        lista.remove(x)
    return lista_nova


# Dado a lista_alunas, vou por ela em ordem alfabetica!
lista_alfabetica = ordena_alpha(lista_alunas)

# Agora que temos a lista na ordem alfabetica, sei que as pontas sao os indices: inicial e final
ponta1 = lista_alfabetica[0]
ponta2 = lista_alfabetica[len(lista_alfabetica) - 1]

# Saida
print(ponta1)
print(ponta2)

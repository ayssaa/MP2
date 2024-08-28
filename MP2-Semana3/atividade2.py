# Problema: my_insert
# Entrada
lista = str(input()).split()
elemento = str(input())
posicao = int(input())
# Fazendo a funcao
def my_insert(lista, elemento, posicao):
    contador = -1
    lista_nova = []
    for i in lista:
        contador += 1
        if contador == posicao:
            lista_nova.append(elemento)
            lista_nova.append(i)
        else:
            lista_nova.append(i)
    return lista_nova
# Saida
if posicao >= len(lista):
  lista.append(elemento)
  print(lista)
else:
  print(my_insert(lista, elemento, posicao))
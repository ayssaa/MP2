# Problema: my_extend
# Entrada
string1 = str(input())
string2 = str(input())
# Transformando em lista
lista1 = string1.split()
lista2 = string2.split()


# Fazendo a funcao
def my_extend(lista1, lista2):
    for i in lista2:
      lista1.append(i)
      return lista1


# Usando a funcao
lista_unida = my_extend(lista1, lista2)
# Saida
print(lista_unida)

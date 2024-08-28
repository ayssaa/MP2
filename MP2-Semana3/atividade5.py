# Problema: my_slicing (2)
# Entrada
string = str(input()).strip()
indices = [int(i) for i in input().split()]
inicio = indices[0]
fim = indices[1]
passo = indices[2]
# Fazendo a funcao
def my_slicing(inicio, fim, passo):
    contador_indice1 = -1
    substring1 = ''
    # Criando substring no parametro inicio/fim
    for i in string:
       contador_indice1 += 1
       if contador_indice1 >= inicio and contador_indice1 < fim:
            substring1 += i
    # Criando dicionario com o passo!
    contador_indice2 = -1
    substring2 = ''
    for i in substring1:
        contador_indice2 += 1
        if contador_indice2 == 0 or (contador_indice2 % passo) == 0:
          substring2 += i
    # Retorna substring
    return substring2
# Saida
print(my_slicing(inicio, fim, passo))
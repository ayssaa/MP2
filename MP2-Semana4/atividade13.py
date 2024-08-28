# Problema: Poderosas na Programação 3
# Entrada: Dado uma lista, achar os 3 maiores valores
lista_input = list(map(int, input().split()))


# Definindo minha função que acha o maior valor
def achar_maior(lista):
    if not lista or len(lista) < 3:
        return False
    # Achando os maiores
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    lista.remove(maior)
    maior2 = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior2:
            maior2 = lista[i]
    lista.remove(maior2)
    maior3 = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior3:
            maior3 = lista[i]
    return maior, maior2, maior3


# Saida
saida = achar_maior(lista_input)
if not saida:
    print('lista pequena demais')
else:
    print(f'{saida[0]} {saida[1]} {saida[2]}')

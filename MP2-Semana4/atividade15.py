# Problema: Dicionarizando
# Entrada: Dado inputs até 'fim' receber strings e criar um dicionário
lista_nome = []
lista_num = []
while True:
    nome = str(input())
    if nome == 'fim':
        break
    else:
        x = nome.split()
        lista_nome.append(x[0])
        lista_num.append(x[1])


# Definindo minha função que transfomrma em dicionário
def dicionarizando(lista1, lista2):
    dicionario = {}
    contador = -1
    for i in lista1:
        contador += 1
        dicionario[i] = int(lista2[contador])
        print(dicionario)
    return True


# Saida e chamando a função
dicionarizando(lista_nome, lista_num)

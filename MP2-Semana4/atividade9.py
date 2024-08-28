# Problema: Nossas Meninas
# Dado uma quantidade de alunas, receber seus nomes e criar uma lista em ordem alfabética
# Recebendo e criando minha lista de nomes (desordenada)
qnt_aluna = int(input())
lista_nome = []
for i in range(qnt_aluna):
    nome = str(input())
    lista_nome.append(nome)


# Criando minha função ordena_alpha
def ordena_alpha(lista):
    lista_ordenada = []
    for numero in range(len(lista)):
        x = min(lista)
        lista_ordenada.append(x)
        lista.remove(x)
    return lista_ordenada


# Chamando a função
print(ordena_alpha(lista_nome))

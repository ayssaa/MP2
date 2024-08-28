# Questão 2 - Prova
# Entrada: Dado inputs crescentes, adicioná-los numa lista COM DEF
lista_nomes = []

def cria_lista(lista):
    while True:
        nome = str(input())
        if nome == '.':
            break
        else:
            lista.append(nome)
    return lista

# Saida
print(cria_lista(lista_nomes))

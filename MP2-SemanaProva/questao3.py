# Questão 3 - Prova
# Entrada: Dado inputs crescentes, adicioná-los numa lista COM DEF E RECURSIVA
lista_bonecas = []


def monta_boneca(lista):
    nome_boneca = str(input())
    if nome_boneca != '.':
        lista.append(nome_boneca)
        monta_boneca(lista)
    return lista


# Saida
print(monta_boneca(lista_bonecas))

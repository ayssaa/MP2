# Questão 1 - Prova
# Entrada: Dado inputs crescentes, adicioná-los numa lista
lista = []
while True:
    nome = str(input())
    if nome == '.':
        break
    else:
        lista.append(nome)

# Saida
print(lista)

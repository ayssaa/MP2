# Problema: Tribunal de contas...
# Listas fixas
lista_pessoais = ['vestido', 'camisa', 'camiseta', 'calça', 'bone']
lista_publicos = ['joia', 'arte', 'arma', 'veiculo']

# Entrada
item_input = str(input())


# Definindo nossa função contagem
def contagem(item):
    itens_pessoais = 0
    itens_publicos = 0
    while item != '!':
        if item in lista_pessoais:
            itens_pessoais += 1
            item = str(input())
        else:
            itens_publicos += 1
            item = str(input())
    return itens_pessoais, itens_publicos


# Usando a função
presentes = contagem(item_input)

# Saida
print(f'itens pessoais: {presentes[0]}')
print(f'itens públicos: {presentes[1]}')

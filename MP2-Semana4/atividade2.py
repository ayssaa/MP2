# Problema: Usando conjuções adversativas
# Entrada
frase_input = str(input()).split()


# Definindo uma função
def conj(frase):
    conjucoes = ['mas', 'porém', 'contudo', 'todavia', 'entretanto']
    for palavra in frase:
        if palavra in conjucoes:
            return palavra
    return False


# Usando a função e printando a saida de acordo com o resultado
if conj(frase_input) is not False:
    print(f'emprega: {conj(frase_input)}')
else:
    print(f'não contém adversativa')

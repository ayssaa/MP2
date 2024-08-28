# Problema: Reconhecendo conjuções adversativas
# Entrada
str_input = str(input())


# Definindo uma função
def conj(string):
    conjucoes = ['mas', 'porém', 'contudo', 'todavia', 'entretanto']
    if string in conjucoes:
        return True
    else:
        return False


# Usando a função e printando a saida de acordo com o resultado
if conj(str_input) is True:
    print('reconheço como conjunção adversativa')
else:
    print('não reconheço como conjunção adversativa')

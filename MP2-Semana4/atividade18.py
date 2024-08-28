# Problema: Respeito apoiado por computador
# Entrada: inputs até 'fim'
fila = []
while True:
    ordem = str(input())
    if ordem == 'fim':
        break
    else:
        fila.append(ordem)


# Criando a função
def prioridade(lista):
    cesta = 0
    pessoa = []
    for nome in lista:
        if nome == '1':
            cesta += 1
            if cesta != 0 and len(pessoa) != 0:
                print(f'agora: {pessoa[0]}')
                pessoa.remove(pessoa[0])
                cesta -= 1
        if nome.isdigit() is False:
            x = nome.replace('0', '')
            pessoa.append(x)
        if len(pessoa) == 0 and cesta == 1:
            cesta = 0
            print(f'agora: pausa para café!')
    return f'fila final: {pessoa}'


print(prioridade(fila))

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
    pessoa_sem = []
    pessoa_com = []
    for nome in lista:
        if nome == '2':
            cesta += 1
            if cesta != 0 and (len(pessoa_com) + len(pessoa_sem)) != 0:
                if (len(pessoa_com)) != 0:
                    print(f'agora: {pessoa_com[0]}')
                    pessoa_com.remove(pessoa_com[0])
                else:
                    print(f'agora: {pessoa_sem[0]}')
                    pessoa_sem.remove(pessoa_sem[0])
                cesta -= 1
        if nome.isdigit() is False:
            if nome.startswith('0'):
                x = nome.replace('0', '')
                pessoa_com.append(x)
            if nome.startswith('1'):
                x = nome.replace('1', '')
                pessoa_sem.append(x)
        if (len(pessoa_com) + len(pessoa_sem)) == 0 and cesta == 1:
            cesta = 0
            print(f'agora: café!')
    return f'fila final com prioridade: {pessoa_com}\nfila final sem prioridade: {pessoa_sem}'


# Chamando a função
print(prioridade(fila))

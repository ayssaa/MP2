# Problema: Eleitores com prioridade
# Entrada: Dado ints até -1 receber idades com e sem prioridade
idade_com = []
idade_sem = []
while True:
    idade = int(input())
    if idade == -1:
        break
    else:
        if idade >= 60:
            idade_com.append(idade)
        else:
            idade_sem.append(idade)

# Saida
print(idade_com)
print(idade_sem)

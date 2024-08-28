# Problema: Sua lista, minha lista
# Entrada
lista_inteiros = list(map(int, str(input()).split()))


# Fazendo minha função ordena
def ordena(lista):
    nova_lista = []
    while True:
        print(f'- {lista}')
        print(f'+ {nova_lista}')
        if len(lista) == 0:
            return
        # Achando qual elemento entrará na nova_lista
        elemento = min(lista)
        # Achando o elemento na nova_lista e removendo da lista
        nova_lista.append(elemento)
        lista.remove(elemento)


# Usando a função
ordena(lista_inteiros)

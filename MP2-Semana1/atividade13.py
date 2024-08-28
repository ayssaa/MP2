#Problema: split()
#Entrada
lista = input()
contador = 0
#Criando as listas
lista_s = []
for s in lista.split():
  lista_s.append(s)
  contador += 1
lista_i = []
for i in lista.split():
  i = int(i)
  lista_i.append(i * 2)
lista_f = []
for f in lista.split():
  f = float(f)
  lista_f.append(f / 2)
#Saida
print(lista_s)
print(lista_i)
print(lista_f)
print(contador)
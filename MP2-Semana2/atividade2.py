# Problema: Poemas ao vento dois
# Entrada
verso = str(input())

# Limpando o verso - tirar pontuacao, aspas duplas
# e simples, considerar tudo minusculo
verso_limpo = ''
for i in verso.lower():
    if i.isalpha() == True or i.isspace() == True:
        verso_limpo += i

# Transformando meu verso_limpo em lista
palavras = verso_limpo.split()

# Dicionario
dicionario = {}

# Colocando as palavras no dicionario e contando
# quando se repete  
for palavra in palavras:
   if palavra not in dicionario:
      dicionario[palavra] = 1
   else:
      dicionario[palavra] += 1

# Saida
print(dicionario)

# Nova entrada
palavra_consultada = str(input())
palavra_consultada_min = palavra_consultada.lower()

# Check para ver se a palavra existe e Saida
if palavra_consultada_min in dicionario:
   print(dicionario[palavra_consultada_min])
else:
   print(f'{palavra_consultada} não encontrada')
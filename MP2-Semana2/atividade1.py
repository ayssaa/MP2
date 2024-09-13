# Problema: Poemas ao vento um
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
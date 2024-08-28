# Problema: my_isdigit()
# Entrada
inteiro_input = str(input())
# Fazendo a funcao
def my_isdigit(inteiro):
 # Definindo o que sao digitos
 digitos = ['0','1','2','3','4','5','6','7','8','9']
 verificando = 0
 for i in inteiro:
   if i not in digitos:
    verificando += 1
 if verificando == 0:
  return True
 else:
  return False
# Saida
print(my_isdigit(inteiro_input))
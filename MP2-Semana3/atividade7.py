# Problema: my_endswith
# Entrada
str1_input = str(input())
str2_input = str(input())
# Fazendo a funcao
def my_endswith(str1, str2):
# Achando o tamanho a str2
 tam_str2 = len(str2)
# Verificando se os digitos da str1 correspondentes ao tam_str2
 if str2 == str1[-tam_str2:]:
  return True
 else: 
  return False
# Saida
print(my_endswith(str1_input, str2_input))
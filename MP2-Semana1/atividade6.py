#Problema: duas vs duas
#Entrada
carta1 = int(input())
carta2 = int(input())
carta3 = int(input())
carta4 = int(input())

dupla1 = [carta1, carta3]
dupla2 = [carta2, carta4]

maior_dupla1 = max(dupla1)
maior_dupla2 = max(dupla2)

#Saida
if maior_dupla1 == maior_dupla2:
  print("empate")
else:
  auxiliar = [maior_dupla1, maior_dupla2]
  print(max(auxiliar))
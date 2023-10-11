from Biblioteca import *
nome = input("DIGITE O NOME DO ALUNO: ")
n1 = float(input(f"DIGITE A  NOTA: "))
n2 = float(input(f"DIGITE A NOTA: "))
a = notas(n1,n2)
print(situação(a,nome))
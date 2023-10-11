from Biblioteca import adicao
qtd = int(input("QUANTOS NUMEROS? "))
l =[0]*qtd
for x in range(qtd):
    l[x] = int(input("DIGITE OS NUMEROS: "))

soma = adicao(l)
print(soma)

from Biblioteca import *
'''Crie uma função que recebe o nome de um produto, a quantidadde
que tem no estoque e o valor unitário do produto.
retorne o valor total do meu estoque'''

nome = input("Nome do produto: ")
qtd = int(input("Quantidade do estoque: "))
vlr = float(input("Valor R$ unt do produto: "))

estoque()
print(estoque(qtd,vlr))
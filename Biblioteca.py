

def estoque (nome,quatidade, valor):
    resultado = quatidade*valor
    return resultado

def notas (n1,n2):
    media = (n1+n2)/2
    return media

def situação (media,nome_aluno):
    if media >= 6:
      return nome_aluno,'Está Aprovado'
    elif media <=4:
        return nome_aluno,'Está Reprovado'
    else:
        return nome_aluno,'Está em Recuperação'

def numero (num):
    if num == 0:
        return 'Z'
    elif num >= 1:
        return 'P'
    else:
        return 'N'

def adicao (args):
    c = 0
    for y in args:
        c += y  # cont = cont + 1
    return c


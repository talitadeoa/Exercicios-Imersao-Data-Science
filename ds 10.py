#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def pn(n):
    if n > 0:
        s = 'P'
    elif n < 0:
        s = 'N'
    else:
        s = '0'
    return s

n = int(input('Digite um número.. '))

if pn(n) in 'P':
    state = 'POSITIVO'
elif pn(n) == 'N':
    state = 'NEGATIVO'
else:
    state = 'VOCE DIGITOU 0'

print(state)
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar(n1,n2,n3):
    r = n1+n2+n3
    return r

n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
n3 = int(input('Digite mais um número '))

print('A soma dos valores inseridos é {}'.format(somar(n1,n2,n3)))
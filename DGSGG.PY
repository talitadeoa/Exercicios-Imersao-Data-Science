if s in 'P':
    state = 'POSITIVO'
elif s == 'N':
    state = 'NEGATIVO'
else:
    state = 'VOCE DIGITOU 0'

print('O valor é {}'.format(state))

-------------------------------------

elif state == 0:
    print('FIM')

while state != 1 and state != 0:
    state = int(input('Para começar digite [1] para encerrar digite [0] '))

#state = int(input('Para tentar novamente digite [1] para encerrar digite [0]))

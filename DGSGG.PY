if s in 'P':
    state = 'POSITIVO'
elif s == 'N':
    state = 'NEGATIVO'
else:
    state = 'VOCE DIGITOU 0'

print('O valor é {}'.format(state))
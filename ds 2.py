# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


g = str(input('Digite a letra correspondente ao seu genero '))

if g in 'f':
    print('Você escolheu F - Feminino')
elif g in 'm':
    print('Você escolher M - Masculino')
elif g in 'n':
    print('Você escolheu N - Não Binário')
else:
    print('Genêro inválido')
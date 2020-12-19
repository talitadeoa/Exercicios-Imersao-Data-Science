# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra ')).lower()

if letra in ['a', 'e', 'i', 'o', 'u']:
    print('{} é uma vogal'.format(letra.upper()))
else:
    print('{} é uma consoante'.format(letra.upper()))
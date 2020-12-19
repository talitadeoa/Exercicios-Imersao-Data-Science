#Faça um programa que leia e valide as seguintes informações:
#* Nome: maior que 3 caracteres;
#* Idade: entre 0 e 150;
#* Salário: maior que zero;
#* Sexo: 'f' ou 'm';
#* Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: R$'))
genero = str(input('Digite seu genêro "F" para Feminino, "M" para masculino, "N" para não binário e "O" para outros ou prefiro não responder ')).upper()
estado = str(input('Digite seu estado civil, "S" para solteiro, "C" para casado, "V" para viuvo" e "D" para divorciado ')).upper()

if len(nome) >= 3 and 150 > idade > 0 and salario > 0 and genero in ['F', 'M', 'N', 'O'] and estado in ['S', 'C', 'V', 'D']:
    print('Boa! Seus dados foram válidados! Obrigado :D')
else: 
    print('Algum dos seu dados não foi validado, tente novamente...')

while len(nome) < 3:
    nome = str(input('Digite seu nome novamente... '))
while 150 < idade or idade < 0:
    idade = int(input('Digite sua idade novamente... '))
while salario < 0:
    salario = float(input('Digite seu salario novamente... '))
while bool(genero in ['F', 'M', 'N', 'O']) == False:
    genero = str(input('Digite seu genêro novamente, "F" para Feminino, "M" para masculino, "N" para não binário e "O" para outros ou prefiro não responder ')).upper()
while bool(estado in ['S', 'C', 'V', 'D']) == False:
    estado = str(input('Digite seu estado civil novamente, "S" para solteiro, "C" para casado, "V" para viuvo" e "D" para divorciado ')).upper()
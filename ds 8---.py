#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

popa = 0
popb = 0
anos = 0
state = 0
crea = 0
creb = 0

while popa <= 0:
    popa = int(input('Digite o valor da população do país A '))
while popb <= 0:
    popb = int(input('Digite o valor da população do país B '))
while crea <= 0:
    crea = float(input('Qual a taxa de crescimento do país A em % '))
    crea = crea/100
while creb <= 0:
    creb = float(input('Qual a taxa de crescimento do país B em % '))
    creb = creb/100

if popa < 0 or popb < 0 or crea < 0 or creb < 0:
    print("Você digitou algum valor inválido, tente novamente ")
else:
    print('Os valores que você digitou foram validados')

while popa < popb or popb < popa:
    anos = anos + 1
    popa = popa + (popa*crea)
    popb = popb + (popb*creb)

print('Levarão {} anos'.format(anos))
print('''População A {}. 
População B {}'''.format(popa, popb))

state = input('Para tentar novamente digite 1 ')

if state == 1:
    popa = 0
    popb = 0
    crea = 0
    creb = 0
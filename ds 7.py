#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

popa = 80000
popb = 200000
crea = 0.03
creb = 0.015
anos = 0

while popa < popb:
        anos = anos + 1
        popa = popa + (popa*crea)
        popb = popb + (popb*creb)

print('Levarão {} anos'.format(anos))
print('''População A {}. 
População B {}'''.format(popa, popb))
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    taxaImposto = custo*taxaImposto/100
    custo = custo+taxaImposto
    return custo

taxaImposto = float(input('Digite o valor do imposto: '))
custo = float(input('E o custo: '))

print('O valor final é {}'.format(somaImposto(taxaImposto,custo)))

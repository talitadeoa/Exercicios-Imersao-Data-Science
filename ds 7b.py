a = int(input("População A = "))

taxaA = float(input("Taxa de crescimento da população A = "))
result1 = (taxaA * 0.01)

b = int(input("\nPopulação B = "))

taxaB = float(input("Taxa de crescimento da população B = "))
result2 = (taxaB * 0.01)

ano = 0

while a <= b:
    a += a * result1
    b += b * result2
    ano += 1

print("\n'A' ultrapassa ou iguala a 'B' em %d anos" %ano)
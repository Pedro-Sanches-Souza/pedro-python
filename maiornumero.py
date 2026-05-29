n1 = int (input("Digite um número: "))
n2 = int (input("Digite outro número:"))
n3 = int (input("Digite outro número:"))
n4 = int (input("Digite outro número:"))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4

print("Maior número: ",maior)
print("Menor número: ",menor)

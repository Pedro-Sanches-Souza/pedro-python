nome =input("Digite o seu nome: ")

idade = int (input("Digite a sua idade: "))

frequencia = float(input("Digite o número de dias que você treina na semana: "))

peso = float(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura: "))

imc = round(peso / (altura * altura),1)

print("========RELATÓRIO========")
print("Nome:",nome)
print("Idade:",idade)
print("Peso:",peso,"Kg")
print("Altura:",altura)

if frequencia >=5:
    print("Dias de treino:", frequencia, "- Excelente frequência!")
elif frequencia >=3:
    print("Dias de treino:", frequencia, "- Boa rotina de treino!")
else:
    print ("Dias de treino:", frequencia, "-Você pode treinar mais para evoluir!")

if imc <18.5:
    print("IMC:",imc, "- Abaixo do peso")
elif imc <=24.9:
    print("IMC:",imc, "- Peso normal")
else:
    print("IMC:",imc, "- Acima do peso")

print("=========================")
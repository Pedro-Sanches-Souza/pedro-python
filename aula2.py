nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

materia = input("Digite o nome da matéria: ")

media = (nota1 + nota2) / 2 

print("\nAluno:", nome)
print("\nMatéria:", materia)
print("\nSua media é:", media)

if media > 9:
    print("\nAluno destaque")


if media >= 6:
    print ("\nAPROVADO")
elif media >= 5:
    print("\nEm recuperação")
    provafinal = float(input("Digite a nota da prova final: "))
    recuperacao = (provafinal + media) / 2
    if recuperacao > 5:
        print ("\nAPROVADO")
        print("\nNota da recuperação: ", recuperacao)
    else:
        print("\nREPROVADO")
        print("\nNota da recuperação: ", recuperacao)
else:
    print ("\nREPROVADO")


      
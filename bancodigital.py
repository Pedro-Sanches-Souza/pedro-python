saldo = 0
saque = 0
deposito = 0
extrato1 = 0
extrato2 = 0

while True:
    print("===== BANCO DIGITAL =====")
    print("\n1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("5 - Sair")
    print("=========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Seu saldo é: ",saldo)


    elif opcao == "2":
        deposito = float(input("Digite o valor que deseja depositar: "))

        if deposito <=0:
            print("Depósito cancelado (o valor precisa ser maior que 0).")
            
        else:
            print("Depósito realizado com sucesso.")
            saldo = (saldo + deposito)
            extrato1 = (extrato1 + deposito)


    elif opcao == "3":
        saque = float(input("Digite o valor que deseja sacar (Máximo de R$500,00): "))
        
        if saque > deposito:
            print("Você não pode sacar mais do que seu saldo.")

        elif saque >500:
            print("Valor excede o limite permitido.")

        else:
            saldo = (saldo - saque)
            extrato2 = (extrato2 - saque)

    
    elif opcao == "4":
        if deposito <= 0 and saque <=0:
            print("Nenhuma movimentação realizada.")

        else:
            print("===== EXTRATO =====")
            print("Depósito: ",extrato1)
            print("Saque: ",extrato2)
            print("===================")

    
    elif opcao == "5":
        print("Sistema encerrado.")
        break


    else:
        print("Digite uma opção válida.")
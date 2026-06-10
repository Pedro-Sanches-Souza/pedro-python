while True:
    print("=============================")
    print("   ESTACIONAMENTO PYTHON")
    print("=============================")

    nome   = input("Nome: ")
    placa  = input("Placa: ")
    modelo = input("Modelo: ")
    cor    = input("Cor: ")

    print("Veículo estacionado com sucesso!")

    horas = int(input("Quantas horas o veículo permaneceu? "))
    valor = 10 + (horas - 1) * 7

    if horas > 8:
        valor = valor * 0.9

    pagamento = input("Forma de pagamento (Se for em PIX ganha 10% de desconto): ")

    if pagamento == "PIX":
        valor = valor * 0.95


    print("=============================")
    print("         RECIBO")
    print("==============================")

    print("Cliente:",nome)
    print("Placa:",placa)
    print("Modelo:",modelo)
    print("Cor:",cor)
    print(f"Tempo: {horas} horas")
    print("Forma de pagamento:",pagamento)
    print(f"Valor a pagar: R$ {valor:.2f}")

    print("Obrigado pela preferência!")

    print("Deseja atender outro cliente?")
    print("1 - Sim")
    print("2 - Não")

    opcao = input("Escolha: ")

    if opcao == "2":
        break
total = 0

while True:
    print("\nTeste")
    total = (total + 1)
    opcao = input("Pausar")
    print("Esse é o total acumulado: ",total)

    if opcao == "S":
        print("O sistema parou")
        break
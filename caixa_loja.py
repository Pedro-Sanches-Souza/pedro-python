total = 0
subtotal = 0
while True:
    print("\n1 - Adicione um produto: ")
    print("2 - Ver carrinho: ")
    print("3 - Finalizar compra: ")
    print("4 - Sair: ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto    = (input("Nome do produto: "))
        valor      = float(input("Valor do produto: "))
        quantidade = int(input("Quantidade: "))
        
        subtotal += (valor * quantidade)
        print ("Esse é o valor subtotal: ",subtotal)

    elif opcao == "2":
        print ("Total atual da compra: ","R$",subtotal)

    elif opcao == "3":
        desconto = 0
        if subtotal >= 100:
            desconto = (subtotal * 0.10)
            total = (subtotal - desconto)
        print ("Total sem desconto: ",subtotal)
        print ("Desconto: ",desconto)
        print ("Total final: ",total)
    
    elif opcao == "4":
        print("Sistema encerrado.")
        break
    
    else:
        print("Opção inválida.")


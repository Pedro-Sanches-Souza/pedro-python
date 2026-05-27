cliente      = input("Digite seu nome: ")
lanche       = input("Digite o lanche que você deseja: ")
quantidade   = int(input("Digite a quantidade de lanches que você deseja: "))
valor        = float(input("Digite o valor de uma unidade do lanche desejado: "))
refrigerante = input("Digite se deseja incluir refrigerante no pedido (S ou N): ")
pagamento    = input("Digite a forma de pagamento (Caso seja em PIX, você recebe 10% de desconto): ")
total        = quantidade * valor


if refrigerante == "S":
    total = (total + 10)

if pagamento == "PIX": 
    total = (total * 0.9)

if total < 30:
    print("Pedido mínimo quase atigindo (30R$)")

if total >= 30:
    if total > 100:
        print("Parabéns! Você ganhou uma sobremesa grátis!")
    
    print("===== PEDIDO =====")
    print("Cliente: ",cliente)
    print("Lanche: ",lanche)
    print("Quantidade: ",quantidade)
    print("Total: ",total,"R$")
    print("==================")
    
    finalizar = input("Deseja finalizar o pedido? (S ou N): ")
    
    if finalizar == "S":
        print("Pedido enviado para cozinha!")
    else:
        print("Pedido cancelado.")
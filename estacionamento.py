import tkinter as tk

def estacionamento():
    global nome
    global placa
    global modelo
    global cor
    global pagamento

    nome      = entrada_nome.get()
    placa     = entrada_placa.get()
    modelo    = entrada_modelo.get()
    cor       = entrada_cor.get()
    pagamento = forma_de_pagamento.get()

    texto_resultado = tk.Label(janela, text="Veículo estacionado com sucesso!", font=("Arial",14), fg="green")
    texto_resultado.pack(pady=20)

    botao.destroy()


    global entrada_horas

    tk.Label(
        janela,
        text="Quantas horas o veículo permaneceu?"
    ).pack()

    entrada_horas = tk.Entry(janela)
    entrada_horas.pack()


    global botao_calcular
    botao_calcular = tk.Button(
        janela,
        text="Calcular valor",
        command=calcular_valor
    )
    botao_calcular.pack()


def calcular_valor():
    horas = int(entrada_horas.get())

    valor = 10 + (horas - 1) * 7

    if horas >8:
        valor = valor * 0.9

    if pagamento == "PIX":
        valor = valor * 0.95

    botao_calcular.destroy()

    tk.Label(
    janela,
    text=f"Cliente: {nome}",
    font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Placa: {placa}",
        font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Modelo: {modelo}",
        font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Cor: {cor}",
        font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Valor a pagar: R$ {valor:.2f}",
        font=("Arial",14) 
        ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Forma de pagamento: {pagamento}",
        font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        janela,
        text=f"Obrigado pela preferência!",
        font=("Arial",14)
    ).pack(pady=10)


janela = tk.Tk()
janela.title("Estacionamento")
janela.geometry("1000x800")


titulo = tk.Label(
    janela, 
    text="Estacionamento Python",
    font=("Arial",16)
    )
titulo.pack(pady=10)


tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Placa:").pack()
entrada_placa = tk.Entry(janela)
entrada_placa.pack()

tk.Label(janela, text="Modelo:").pack()
entrada_modelo = tk.Entry(janela)
entrada_modelo.pack()

tk.Label(janela, text="Cor:").pack()
entrada_cor = tk.Entry(janela)
entrada_cor.pack()

tk.Label(janela, text="Forma de pagamento:").pack()
forma_de_pagamento = tk.Entry(janela)
forma_de_pagamento.pack()


botao = tk.Button(
    janela,
    text="Concluir",
    command=estacionamento,
    )
botao.pack(pady=15)


janela.mainloop()
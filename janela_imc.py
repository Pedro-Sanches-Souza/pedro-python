import tkinter as tk

def calcular_imc():
    nome = entrada_nome.get()
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())

    imc = peso / (altura * altura)

    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    else:
        resultado = "Obesidade"
    
    texto_resultado.config(
        text=f"{nome}, seu imc é {imc:.2f}\n classificação: {resultado}"
    )


janela = tk.Tk()
janela.title("Calculadora de imc")
janela.geometry("600x400")


titulo = tk.Label(
    janela, 
    text="Calculadora de IMC",
    font=("Arial",16)
    )
titulo.pack(pady=10)

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Peso:").pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

tk.Label(janela, text="Altura:").pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()

botao = tk.Button(
    janela,
    text="Calcular imc",
    command=calcular_imc
)
botao.pack(pady=15)

texto_resultado = tk.Label(janela, text="", font=("Arial",14), fg="Red")
texto_resultado.pack(pady=20)

janela.mainloop()
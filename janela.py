import tkinter as tk

def clicar():
    mensagem.config(text="Olá Pedro! Você clicou na opção")

janela = tk.Tk()
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="Bem vindo a aula",
    font=("Arial",16)
)
titulo.pack(pady=20)

mensagem = tk.Label(
    janela,
    text="oi"
)

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=clicar
)
botao.pack()

mensagem.pack(pady=20)

janela.mainloop()
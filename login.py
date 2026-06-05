import tkinter as tk

tentativas = 0

def login():
    global tentativas

    usuario        = entrada_usuario.get()
    senha          = float (entrada_senha.get())
    usuariocorreto = "pedro"
    senhacorreta   = 1234


    if usuario == usuariocorreto and senha == senhacorreta:
        tentativas = 0

        texto_resultado = tk.Label(janela, text="Bem vindo ao sistema!", font=("Arial",14), fg="green")
        texto_resultado.pack(pady=20)

        entrada_usuario.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)

    else:
        if tentativas > 2:
            texto_resultado = tk.Label(janela, text="Sistema bloqueado.", font=("Arial",14), fg="red")
            texto_resultado.pack(pady=20)

            entrada_usuario.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)
        

        else:
            tentativas = (tentativas + 1)

            texto_resultado = tk.Label(janela, text="Usuário ou senha inválidos.", font=("Arial",14), fg="red")
            texto_resultado.pack(pady=20)

            entrada_usuario.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)


janela = tk.Tk()
janela.title("Login")
janela.geometry("600x400")


titulo = tk.Label(
    janela, 
    text="Login",
    font=("Arial",16)
    )
titulo.pack(pady=10)


tk.Label(janela, text="Usuário:").pack()
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

tk.Label(janela, text="Senha:").pack()
entrada_senha = tk.Entry(janela)
entrada_senha.pack()


botao = tk.Button(
    janela,
    text="Entrar",
    command=login
)
botao.pack(pady=15)

botao = tk.Button(
    janela,
    text="Sair",
    command=janela.destroy
)
botao.pack(pady=15)


janela.mainloop()
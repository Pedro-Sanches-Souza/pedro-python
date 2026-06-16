import tkinter as tk
import psycopg2


def login():
    global nome
    global email
    global senha

    nome  = entrada_nome.get()
    email = entrada_email.get()
    senha = entrada_senha.get()

    resultado_valido = validar_login(nome, email, senha)

    if resultado_valido:
        texto_resultado = tk.Label(janela, text="Login concluído!", font=("Arial",14), fg="green")
        texto_resultado.pack(pady=20)

        texto_saudacao = tk.Label(janela, text=f"Bem vindo {nome}!", font=("Arial",14))
        texto_saudacao.pack(pady=20)

        botao_entrar.destroy()

    else:
        texto_resultado = tk.Label(janela, text="Email ou senha inválidos.", font=("Arial",14), fg="red")
        texto_resultado.pack(pady=20)

        entrada_nome.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)


def conectar():
    return psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "postgres",
        user = "postgres",
        password = "segredo847"
    )


def validar_login(nome, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT nome
    FROM usuario
    WHERE email = %s
    AND senha = %s
""", (email, senha))
    
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()
    return resultado


janela = tk.Tk()
janela.title("Sistema de login")
janela.geometry("1000x800")


titulo = tk.Label(
    janela,
    text="Login",
    font=("Arial",16)
    )
titulo.pack(pady=10)


tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Email").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Label(janela, text="Senha").pack()
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()


botao_entrar = tk.Button(
    janela,
    text="Entrar",
    command=login
)
botao_entrar.pack(pady=15)

botao_cancelar = tk.Button(
    janela,
    text="Cancelar",
    command=janela.destroy
)
botao_cancelar.pack(pady=15)


janela.mainloop()

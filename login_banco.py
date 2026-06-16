import psycopg2

def conectar():
    return psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "postgres",
        user = "postgres",
        password = "segredo847"
    )

def validar_login(email, senha):
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

print("--Login--")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

usuario = validar_login(email, senha)

if usuario:
    print("Você está logado.")
else:
    print("Email ou senha invalidos.")
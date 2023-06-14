import hashlib
import os

diretorio_atual = os.getcwd()
caminho_arquivo = os.path.join(diretorio_atual, "usuarios.txt")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário (até 20 caracteres): ")
    senha = input("Digite a senha do usuário (4 caracteres): ")

    if len(nome) > 20 or len(senha) != 4:
        print("Erro: Nome deve ter até 20 caracteres e senha deve ter 4 caracteres.")
        return

    senha_hash = hashlib.md5(senha.encode()).hexdigest()


    with open(caminho_arquivo, "a") as file:
        file.write(f"{nome},{senha_hash}\n")

    print("Usuário cadastrado com sucesso!")

def autenticar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    senha_hash = hashlib.md5(senha.encode()).hexdigest()

    with open(caminho_arquivo,"r") as file:
        for line in file:
            usuario, senha_armazenada = line.strip().split(",")
            print(line)
            if usuario == nome and senha_armazenada == senha_hash:
                print("Autenticação bem-sucedida!")
                return

    print("Nome de usuário ou senha incorretos.")

def main():
    if not os.path.isfile("usuarios.txt"):
        open("usuarios.txt", "w").close()

def main():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Autenticar usuário")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            autenticar_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "main":
    main()
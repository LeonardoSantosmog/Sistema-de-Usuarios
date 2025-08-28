print("---Sistema De Usuarios---")
print("Bem Vindo ao Sistema De Usuarios")

while True:
    print("1 - Cadastrar usuario: ")
    print("2 - Listar usuarios: ")
    print("3 - Remover usuario: ")
    print("0 - sai do programa: ")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuario: ")
        idade = input("Digite a idade do usuario: ")

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome},{idade}\n")
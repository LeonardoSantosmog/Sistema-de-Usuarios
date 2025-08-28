# 🚀 Sistema de Usuários

![Sistema de Usuários](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)  
Um sistema simples e intuitivo para gerenciar usuários diretamente pelo terminal, feito em **Python**. Ideal para iniciantes que querem praticar manipulação de listas e interação com o usuário.

---

## ✨ Funcionalidades

- 🆕 Cadastrar novos usuários
- 📋 Listar usuários cadastrados
- ❌ Remover usuários pelo nome
- 🚪 Sair do programa com segurança

---

## 🛠️ Código Fonte

```python
print("-----Sistema De Usuarios-----")
print("Bem vindo...")

usuario = []

while True:
    print("1 - Cadastrar Usuario: ")
    print("2 - Listar Usuarios: ")
    print("3 - Remover Usuários: ")
    print("0 - Sair do Programa: ")

    opcao = input("Digite a opção: ")

    if opcao  == "1":
        novo_usuario = input("Digite o novo Usuario: ")
        usuario.append(novo_usuario)
        print(f"{novo_usuario} Adicionado com sucesso")
    elif opcao == "2":
        for i, usuarios in enumerate(usuario, start=1):
            print(f"{i}. {usuarios}")
    elif opcao == "3":
        remover_usuario = input("Digite o codigo do usuario: ")
        usuario.remove(remover_usuario)
        print(f"{remover_usuario} removido com sucesso!!! ")
    elif opcao == "0":
        break

---------------------------------------------------------------------------

-----Sistema De Usuarios-----
Bem vindo...

1 - Cadastrar Usuario: 
2 - Listar Usuarios: 
3 - Remover Usuários: 
0 - Sair do Programa: 
Digite a opção: 1
Digite o novo Usuario: Maria
Maria Adicionado com sucesso

1 - Cadastrar Usuario: 
2 - Listar Usuarios: 
3 - Remover Usuários: 
0 - Sair do Programa: 
Digite a opção: 2
1. Maria

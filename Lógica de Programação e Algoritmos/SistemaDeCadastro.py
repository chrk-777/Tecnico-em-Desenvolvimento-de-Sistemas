# Sistema de cadastro de usuários e produtos
# O sistema deverá permitir:
# - Cadastrar
# - listar 
#- deletar

# Criação das listas
usuarios = []
produtos = []

# ----------------------------------
# ------ função Menu Usuários-------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("----- Menu Usuário -----")
        print("1 - Cadastrar Usuário")
        print("2 - listar Usuário")
        print("3 - deletar Usuário")
        print("4 - Voltar")

        opcao_menu_usuario = int(input("Escolha uma opção: "))

        match opcao_menu_usuario:
            # Cadastrar Usuários
            case 1:
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                email = input("Digite o email: ")
                
                # Criação do json de usuários (chave: valor)
                usuario = {
                    "nome": nome, 
                    "telefone": telefone,
                    "email":email

                }

                # Adicionar o json de array
                usuarios.append(usuario)
                print(f"usuarios{usuario["nome"]} cadastrar com sucesso!")
            case 2:
                print("\n Lista de usuarios: ")

                if(len(usuarios) == 0):
                    print("Nenhum usuário cadastrado!")
                else: 
                    for usu in usuarios:
                        print("---------")
                        print("nome: ", usu["nome"])
                        print("email: ", usu["email"])
                        print("telefone: ", usu["telefone"])
            # deletar usuário
            case 3:
                nome_deletar = input("Digite o nome do usuário que deseja deletar:")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("usuarios removidos com sucesso!")
                if(encontrado == False):
                    print("usuário não encontrado")


            # Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break

def menu_usuarios():
    opcao_menu_produtos= 0

    while(opcao_menu_produtos != 4):
        print()
        print("----- Menu Produto -----")
        print("1 - Cadastrar Produto")
        print("2 - listar Produto")
        print("3 - deletar Produto")
        print("4 - Voltar")

        opcao_menu_produto = int(input("Escolha uma opção: "))

        match opcao_menu_produtos:
            # Cadastrar Produtos
            case 1:
                nome = input("Digite o nome: ")
                descricao = input("Digite o descricao: ")
                quantidade = input("Digite o quantidade: ")
                valor = float(input("Digite o valor: "))
                
                # Criação do json de produto (chave: valor)
                produto = {
                    "nome": nome, 
                    "descricao": descricao,
                    "quantidade":quantidade,
                    "valor": valor

                }

                # Adicionar o json de array
                produto.append(produto)
                print(f"produto{produto["nome"]} cadastrar com sucesso!")
            case 2:
                print("\n Lista de produtos: ")

                if(len(produtos) == 0):
                    print("Nenhum produtos cadastrado!")
                else: 
                    for pro in produtos:
                        print("---------")
                        print("nome: ", pro["nome"])
                        print("descricao: ", pro["descricao"])
                        print("quantidade: ", pro["quantidade"])
                        print("valor: ", pro["valor"])
                # deletar produtos
            case 3:
                nome_deletar = input("Digite o nome do produto que deseja deletar:")
                encontrado = False

                for pro in produtos:
                    if(pro["nome"] == nome_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("produtos removidos com sucesso!")
                if(encontrado == False):
                    print("produto não encontrado")


            # Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
# ----------------------------------
# ---------- Menu principal---------
opcao_menu = 0
while(opcao_menu != 3):
    print("----- Menu - Sistemas de Cadastro -----")
    print("1 - usuarios")
    print("2 - Produtos")
    print("3 - Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        # Menu Usuários
        case 1:
            menu_usuarios()
        # Menu Produtos
        case 2:
            print("Produtos")
        case 3:
            print("👍🏻 Até logo!")
        case _:
            print("✖️ Opção inválida")
# Sistema de cadastro de usuarios e produtos 
# O sistema devera permitir 

# - cadastrar 
# - Listar 
# - deletar 



# - Tipo de Ingresso

# Criação de listas 
usuarios = []
filmes = []

def gerar_resumo (tipo, valor):
    print("Tipo de Ingresso: ", tipo)
    print("valor do Ingresso: ", valor)

def desconto(valor):
    tem_desconto = input("Você tem um desconto? ")

    if(tem_desconto == "Sim"):
        print("Valor do ingresso com desconto: ", valor*0.9)


print("------------------Menu Ingresso--------------------")
print("1- Normal")
print("2- Estudante")
print("3- Idoso")
opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        gerar_resumo("Normal",30)
        desconto(30)
    case 2:
        gerar_resumo("Estudante",10)
        desconto(10)
    case 3:
        gerar_resumo("Idoso", 20)
        desconto(20)
    case _:
        print("Opção inválida!")


#-----------------------------------------
# ---------Função menu ususario----------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("----------Menu Usuários----------")
        print("1 - Cadastrar Usuários")
        print("2 - Listar usuários")
        print("3 - Deletar usuário ")
        print("4 - Voltar")

        opcao_menu_usuario = int(input("Digite uma opção: "))

        match opcao_menu_usuario:
            # Cadastrar ususario
            case 1: 
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                email = input("Digite o email: ")
                cpf= int(input("Digite seu CPF"))
            
                # Criação do json de usuarios (cahve: valor)
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email,
                    "cpf": cpf 
                }
                
                #Adicionar o json no array
                usuarios.append(usuario)
                print(f"Usuario {usuario['nome']} cadastrado com sucesso!")
            # Listar usuarios
            case 2: 
                print("\n Lista de Usuarios: ")

                if(len(usuarios) == 0):
                    print("Nenhum usuário cadastrado!")
                else:
                    for usu in usuarios:
                        print("--------------------")
                        print("Nome: ", usu["nome"])
                        print("Telefone: ", usu["telefone"])
                        print("email: ", usu["email"])
                        print("cpf: ", usu["cpf"])

            # Deletar usuario
            case 3:
                nome_deletar = input("Digite o nome do usuario que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuario removido com sucesso!")
                if(encontrado == False):
                    print("usuario não encontrado")

            # Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break
            # ---------Função menu produtos----------
def menu_filmes():
    opcao_menu_filmes = 0

    while(opcao_menu_filmes != 5):
        print()
        print("----------Menu Filmes----------")
        print("1 - Cadastrar Filmes")
        print("2 - Listar Filmes")
        print("3 - Deletar Filme ")
        print("5 - Voltar")

        opcao_menu_filmes = int(input("Digite uma opção: "))

        match opcao_menu_filmes:
            # Cadastrar filme
            case 1: 
                nome = input("Digite o nome: ")
                descricao = input("Digite a descricao: ")
        
                # Criação do json de usuarios (cahve: valor)
                filme = {
                    "nome": nome,
                    "descricao": descricao
                    
                }
                
                #Adicionar o json no array
                filmes.append(filme)
                print(f"filme {filmes['nome']} cadastrado com sucesso!")
            # Listar Produtos
            case 2: 
                print("\n Lista de filme: ")

                if(len(filmes) == 0):
                    print("Nenhum produto cadastrado!")
                else:
                    for fil in filmes:
                        print("--------------------")
                        print("Nome: ", fil["nome"])
                        print("descricao: ", fil["descricao"])
                        print("quantidade: ", fil["quantidade"])
                        print("valor", fil ["Valor"])

            # Deletar filme
            case 3:
                filme_deletar = input("Digite o nome do filme que deseja deletar: ")
                encontrado = False

                for fil in filmes:
                    if(fil["nome"] == filme_deletar):
                        filmes.remove(fil)
                        encontrado = True
                        print("filme removido com sucesso!")
                if(encontrado == False):
                    print("Produto não encontrado")

            # Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break



# ---------------------------------------------
# ----------menu principal----------
opcao_menu = 0
while(opcao_menu != 3):
    print("---------------Menu - sistema de casdastro--------------")
    print("Opções: ")
    print("1- Usuários")
    print("2- filmes")
    print("3- Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        # Menu usuarios 
        case 1:
            menu_usuarios()
        #Menu Produto
        case 2:
            menu_filmes()
        case 3:
            print("Até logo!")
        case _:
            print("Opção inválida!")



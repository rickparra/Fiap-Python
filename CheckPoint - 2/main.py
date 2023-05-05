#Definindo lista do estoque
produtos = []

# Função para dar as boas-vindas e registrar informações da empresa
def boas_vindas():
    print("Bem-vindo ao sistema de controle de estoque!")
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da empresa: ")
    empresa = (nome, cnpj)
    return empresa

# Função que exibe o menu principal e redireciona para as opções escolhidas
def menu_principal():
    print("=== MENU ===")
    print("1. Menu estoque")
    print("2. Menu compras")
    print("3. Sair")

    opcao = (input("Escolha uma opção: "))

    # Substituição do if pelo match case para redirecionar para as funções de acordo com a opção escolhida
    match opcao:
        case '1':
            menu_estoque()
        case '2':
            menu_compras()
        case '3':
            print("Obrigado por utilizar o sistema!")
            exit()  # Encerra o programa
        case _:
            print("Opção inválida! Tente novamente.")
    menu_principal()

#Função que exibe o menu de compras
def menu_compras():
    print("=== MENU COMPRAS ===")
    print("1. Comprar item")
    print("2. Sair")
    print("3. Voltar ao menu principal")

    opcao = (input("Escolha uma opção: "))

    # Substituição do if pelo match case para redirecionar para as funções de acordo com a opção escolhida
    match opcao:
        case '1':
            adiciona_estoque()
        case '2':
            print("Obrigado por utilizar o sistema!")
            exit()  # Encerra o programa
        case '3':
            print("Voltando...")
            menu_principal()
        case _:
            print("Opção inválida! Tente novamente.")
    menu_compras()


#Função que exibe o menu para estoque
def menu_estoque():
    print("=== MENU ESTOQUE ===")
    print("1. Remover item do estoque")
    print("2. Visualizar estoque")
    print("3. Modificar quantidade de um item do estoque")
    print("4. Sair")
    print("5. Voltar ao menu principal")
    opcao = (input("Escolha uma opção: "))

    # Substituição do if pelo match case para redirecionar para as funções de acordo com a opção escolhida
    match opcao:
        case '1':
            remove_estoque()
        case '2':
            visualiza_estoque()
        case '3':
            modifica_estoque()
        case '4':
            print("Obrigado por utilizar o sistema!")
            exit()  # Encerra o programa
        case '5':
            print("Voltando...")
            menu_principal()
        case _:
            print("Opção inválida! Tente novamente.")
            menu_estoque()

# Função para adicionar produto ao estoque
def adiciona_estoque():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto: "))

    # Confirmação da adição antes de adicionar o produto à lista
    if confirmar_compra():
        produto = (nome, descricao, preco, qtd)
        produtos.append(produto)
        print("Produto adicionado com sucesso!")
    else:
        print("Compra cancelada.")
    menu_compras()

# Função para remover produto do estoque
def remove_estoque():
    if not produtos:
        print("Não há produtos em estoque!")
        menu_estoque()
        return
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto[0] == nome:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            break
    else:
        print("Produto não encontrado!")
    menu_estoque()

# Função para exibir os produtos em estoque
def visualiza_estoque():
    print("Produtos em estoque:")
    print("")
    for produto in produtos:
        print(f"Nome: {produto[0]} | Descrição: {produto[1]} | Preço: R${produto[2]:.2f} | Quantidade: {produto[3]} ")
    menu_estoque()

#Função para modificar a quantidade de um item no estoque
def modifica_estoque():
    nome = input("Digite o nome do produto que deseja modificar: ")
    for i, produto in enumerate(produtos):
        if produto[0] == nome:
            print(f"Produto encontrado: {produto}")
            novo_qtd = input("Digite a nova quantidade: ")
            produtos[i] = (produto[0], produto[1], produto[2], int(novo_qtd))
            print("Quantidade modificada com sucesso!")
            break
    else:
        print("Produto não encontrado!")
    menu_estoque()

# Função para confirmar compra
def confirmar_compra():
    while True:
        resposta = input("Deseja confirmar a compra? (s/n) ")
        if resposta.lower() == "s":
            return True
        elif resposta.lower() == "n":
            return False
        else:
            print("Resposta inválida! Digite s para sim ou n para não.")

# Execução das funções de boas-vindas e menu
boas_vindas()
menu_principal()


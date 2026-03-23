produtos = []

class Produto():
    def __init__(self, nome_produto, valor, descricao, disponivel):
        self.nome_produto = nome_produto
        self.valor = valor
        self.descricao = descricao
        self.disponivel = disponivel

    
def cadastrar_produto():
    nome = str(input("\nDigite o nome do produto: ")).title()
    valor = float(input("Digite o valor do produto: "))
    descricao = input("Digite a descrição do produto: ").title()
    disponivel = input("Esse produto está disponível? (s/n): ").lower() == "s"

    if disponivel is True:
        disponivel = "Disponível"
    else:
        disponivel = "Indisponível"

    novo_produto = Produto(nome, valor, descricao, disponivel)
    return novo_produto



def listar_produto():
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    print("\n-----Lista de produtos-----")
    for id, produto in enumerate(produtos, start=1):
        valor_formatado = f"R${produto.valor:.2f}"
        print(f'{id}. {produto.nome_produto} | {valor_formatado} | {produto.descricao} | {produto.disponivel}')    


def atualizar_produto():
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    
    listar_produto()

    atualizar = int(input("\nDigite o número de um produto para atualizar: "))
    indice = atualizar - 1
    if 0 <= indice < len(produtos):
        produto = produtos[indice]
        nome_atualizado = str(input("\nDigite o novo nome do produto: "))
        valor_atualizado = float(input("Digite o novo valor: "))
        descricao_atualizado = input("Digite a nova descrição: ")
        disponivel_atualizado = input("Esse produto está disponível? (s/n): ").lower() == "s"
    
        if disponivel_atualizado is True:
            disponivel_atualizado = "Disponível"
        else:
            disponivel_atualizado = "Indisponível"

        produto.nome_produto = nome_atualizado
        produto.valor = valor_atualizado
        produto.descricao = descricao_atualizado
        produto.disponivel = disponivel_atualizado
    
        print("\nProduto atualizado com sucesso!")
    else:
        print("\nProduto não encontrado!")    


def remover_produto():
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    listar_produto()
    remover = int(input("\nDigite o número do produto que quer remover: "))
    indice = remover - 1
    if 0 <= indice < len(produtos):
        produto = produtos[indice]
        produtos.remove(produto)
        print("\nProduto removido com sucesso!")
    else:
        print("\nNúmero inválido!")

while True: 
    print("\n------Menu------")
    menu = int(input("\n1. Criar\n2. Listar\n3. Atualizar\n4. Remover\n0. Sair\n \nDigite um número para uma ação: " ""))

    if menu == 1:
        novo_produto = cadastrar_produto()
        produtos.append(novo_produto)
        print("\nProduto criado com sucesso!\n")
    elif menu == 2:
        listar_produto()
    elif menu == 3:
        atualizar_produto()
    elif menu == 4:
        remover_produto()
    elif menu == 0:
        print("\nEncerrando...")
        break
    else:
        print("\nOpção Inválida!")
#Programa de controle de estoque

ESTOQUE = "estoque_produtos.txt"

def le_arquivo():
    try:
        arq = open(ESTOQUE, "r+")
        print('\n' + arq.read())
        arq.close()
    except IOError:
        print("Desculpe arquivo não encontrado")

def escrevendo_no_arquivo(texto):
    try:
        arq = open(ESTOQUE, "a+")
        arq.writelines('\n'+texto)
        arq.close()
        print("\n Registro gravado com sucesso!")
    except IOError:
        print("\n Erro ao abrir o arquivo, por favor tente de novo.")


opcao=""
while opcao != 4 :
    print(15*"*", "Bem vindo", 15*"*")
    print("- Por favor escolha a opção desejada -")
    print("1 - Cadastrar Produto")
    print("2 - Listar os Produtos Cadastrados")
    print("3 - Remover produtos Cadastrados")
    print("4 - Sair")
    opcao = int(input("# Por favor digite o número da opção desejada: "))

    if opcao == 1:
        print("\n \n*** Muito bem, você escolheu a opção de Cadastrar produto ****")
        print("\n \n*** Por favor informe a baixo as especificações ***")
        nome_do_produto = input("Digite o nome do produto - ex: 'Malback/Booticario': ")
        quantidade_do_produto = input("Digite agora a quantidade disponivel do produto: ")
        data_de_validade = input("Digite a data de validade do produto - ex: 12/12/2020 : ")
        cop = ('\n Produto - '+nome_do_produto+ '\n Quantidade - '+quantidade_do_produto+ '\n Data de validade - '+data_de_validade)
        escrevendo_no_arquivo(str(cop))

    elif opcao == 2:
        print("*** Os produtos cadastrados são ***")
        le_arquivo()

    elif opcao == 3:
        print("\n\n\n :( *** Opa, parece que ocorreu um ERRO inesperado ***")
        print("Por favor exclua o produto diretamente do arquivo .txt\n\n")
        

    elif opcao == 4:
        print("\n Saindo do programa ...")
        print("\n Obrigado pela espera")
        print("\n \n PROGRAMADOR -  LUCAS ARAGÃO")

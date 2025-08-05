
# A - Implementar o print com uma mensagem de boas-vindas que apareça o seu nome.
print("bem vindo a livraria de Arthur Vinicius")

# B - Implementar uma lista vazia chamada lista_livro e uma variável id_global com valor inicial igual a 0.
lista_livro = []
id_global = 0

# C - Implementar uma função chamada cadastrar_livro(id).
def cadastrar_livro(id):
    # C.a - Pergunta nome, autor, editora do livro.
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    # C.b - Armazena o id (fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário.
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    # C.c - Copiar o dicionário para dentro da lista_livro.
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# D - Implementar uma função chamada consultar_livro().
def consultar_livro():
    while True:
        # D.a - Perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu).
        print("Consultar Livro:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # D.a.1 - Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados.
            print("Lista de todos os livros:")
            for livro in lista_livro:
                print(livro)
        elif opcao == '2':
            # D.a.2 - Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados.
            id_consulta = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(livro)
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado")
        elif opcao == '3':
            # D.a.3 - Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados.
            autor_consulta = input("Digite o autor do livro: ")
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_consulta.lower()]
            if encontrados:
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para o autor")
        elif opcao == '4':
            # D.a.4 - Se Retornar ao menu, deve-se retornar ao menu principal.
            break
        else:
            # D.b - Se entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta.
            print("Opção inválida")

# E - Implementar uma função chamada remover_livro().
def remover_livro():
    while True:
        try:
            # E.a - Perguntar pelo id do livro a ser removido.
            id_remove = int(input("Digite o ID do livro a ser removido: "))
            # E.b - Remover o livro da lista_livro.
            livro_encontrado = next((livro for livro in lista_livro if livro["id"] == id_remove), None)
            if livro_encontrado:
                lista_livro.remove(livro_encontrado)
                print("Livro removido com sucesso!")
                break
            else:
                # E.c - Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta.
                print("Id inválido. Tente novamente.")
        except ValueError:
            print("Id inválido. Tente novamente.")

# F - Implementar uma estrutura de menu no código principal.
while True:
    # F.a - Perguntar qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa).
    print("Menu")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # F.a.1 - Se Cadastrar Livro, acrescentar em um id_global e chamar a função cadastrar_livro(id_global).
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        # F.a.2 - Se Consultar Livro, chamar função consultar_livro().
        consultar_livro()
    elif opcao == '3':
        # F.a.3 - Se Remover Livro, chamar função remover_livro().
        remover_livro()
    elif opcao == '4':
        # F.a.4 - Se Encerrar Programa, sair do menu (e com isso acabar a execução do código).
        print("Finalizando o programa...")
        break
    else:
        # F.b - Se entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta.
        print("Opção inválida. Tente novamente.")

# G - Implementar uma lista de dicionários.

# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.

# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 4) Alterar nome
#  ---> O usuario digita o nome que deseja alterar, mostra a posição do nome e pede o novo nome que será colocado
# 5) Excluir nome
#  ---> Perguntar  se o usuário tem certeza que deseja excluir, sem usar o método remove()
# 0) Sair do programa
# ——————–
# Digite sua escolha:_

# Função que remove o item de uma lista, recebe a lista e o índice do item e retorna a lista com o item removido
def remove_item(lista, indice_item):
    if not isinstance(lista, list) or not isinstance(indice_item, int):
        return Exception
    if indice_item < 0 or indice_item >= len(lista):
        return Exception

    lista[indice_item] = ''
    lista_nova = []
    for i in lista:
        if i != '':
            lista_nova.append(i)
    return lista_nova

# Função que altera um nome existente na lista por um novo
def alterar_nome(lista, nome_antigo, nome_novo):
    if not isinstance(lista, list) or not isinstance(nome_antigo, str) or not isinstance(nome_novo, str):
        return Exception
    if nome_antigo not in lista:
        return Exception
    indice = lista.index(nome_antigo)
    lista[indice] = nome_novo
    return lista

# Função que pesquisa um nome e retorna sua posição (1-indexed)
def pesquisar_nome(lista, nome):
    if not isinstance(lista, list) or not isinstance(nome, str):
        return Exception
    if nome not in lista:
        return Exception
    return lista.index(nome) + 1

# Função que adiciona um nome se houver espaço na lista (tamanho limitado)
def cadastrar_nome(lista, nome, limite):
    if not isinstance(lista, list) or not isinstance(nome, str) or not isinstance(limite, int):
        return Exception
    if len(lista) >= limite:
        return Exception
    lista.append(nome)
    return lista

def main():
    lista = []
    limite = 5

    # Teste cadastro válido
    assert cadastrar_nome(lista, "Ana", limite) == ["Ana"]
    assert cadastrar_nome(lista, "Bia", limite) == ["Ana", "Bia"]
    assert cadastrar_nome(lista, "Caio", limite) == ["Ana", "Bia", "Caio"]

    # Teste pesquisa
    assert pesquisar_nome(lista, "Bia") == 2
    assert pesquisar_nome(lista, "Caio") == 3

    # Teste alteração
    assert alterar_nome(lista, "Bia", "Beatriz") == ["Ana", "Beatriz", "Caio"]

    # Teste exclusão
    assert remove_item(lista, 1) == ["Ana", "Caio"]

    # Testes de exceções
    assert cadastrar_nome("não é lista", "João", 3) == Exception
    assert cadastrar_nome(lista, "Daniel", "limite errado") == Exception
    assert cadastrar_nome(lista, "Pedro", 2) == Exception  # limite já foi ultrapassado

    assert pesquisar_nome(lista, 123) == Exception
    assert pesquisar_nome("texto", "Ana") == Exception
    assert pesquisar_nome(lista, "Inexistente") == Exception

    assert alterar_nome(lista, "NomeFalso", "Novo") == Exception
    assert alterar_nome("erro", "Ana", "Nova") == Exception

    assert remove_item("não é lista", 0) == Exception
    assert remove_item(lista, 100) == Exception
    assert remove_item(lista, -1) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
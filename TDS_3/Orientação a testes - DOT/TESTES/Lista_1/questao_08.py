# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def ler_escolha(caractere):
    if not isinstance(caractere, str):
        return Exception

    caractere = caractere.upper()
    if caractere == "S":
        return "S"
    elif caractere == "N":
        return "N"
    else:
        return Exception

def cubo(num):
    if not isinstance(num, (int, float)):
        return Exception
    return num ** 3

def main():
    # TESTES DO CUBO
    assert cubo(2) == 8
    assert cubo(3.0) == 27.0
    assert cubo(-1) == -1
    assert cubo("a") == Exception
    assert cubo(None) == Exception

    # TESTES DO LER_ESCOLHA
    assert ler_escolha("S") == "S"
    assert ler_escolha("s") == "S"
    assert ler_escolha("N") == "N"
    assert ler_escolha("n") == "N"
    assert ler_escolha("X") == Exception
    assert ler_escolha("") == Exception
    assert ler_escolha(1) == Exception
    assert ler_escolha(None) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()

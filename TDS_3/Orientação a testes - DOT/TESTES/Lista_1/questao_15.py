# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(N^2+1)/(N+3)

def calcula_formula(num):
    if not isinstance(num, int) or num <= 0:
        return Exception

    soma = 0
    for i in range(1, num + 1):
        soma += (i**2 + 1) / (i + 3)
    return soma

def main():
    # ACERTOS
    assert round(calcula_formula(1), 2) == round((1**2 + 1) / (1 + 3), 2)
    assert round(calcula_formula(2), 2) == round((1**2 + 1) / (1 + 3) + (2**2 + 1) / (2 + 3), 2)
    assert round(calcula_formula(3), 2) == round((1**2 + 1) / (1 + 3) + (2**2 + 1) / (2 + 3) + (3**2 + 1) / (3 + 3), 2)
    assert round(calcula_formula(5), 2) == round(
        (1**2 + 1) / (1 + 3) + (2**2 + 1) / (2 + 3) + (3**2 + 1) / (3 + 3) + (4**2 + 1) / (4 + 3) + (5**2 + 1) / (5 + 3), 2
    )

    # ERROS
    assert calcula_formula(0) == Exception
    assert calcula_formula(-1) == Exception
    assert calcula_formula("abc") == Exception
    assert calcula_formula(3.14) == Exception
    assert calcula_formula(None) == Exception
    assert calcula_formula([]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()


# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

def calcula_formula(num):
    if not isinstance(num, int) or num <= 0:
        return Exception

    soma = 0
    for i in range(1, num + 1):
        soma += 1 / i
    return soma

def main():
    # ACERTOS
    assert round(calcula_formula(1), 2) == 1.00
    assert round(calcula_formula(2), 2) == 1.50
    assert round(calcula_formula(3), 2) == 1.83
    assert round(calcula_formula(5), 2) == 2.28
    assert round(calcula_formula(10), 2) == 2.93

    # ERROS
    assert calcula_formula(0) == Exception
    assert calcula_formula(-1) == Exception
    assert calcula_formula("a") == Exception
    assert calcula_formula(3.5) == Exception
    assert calcula_formula(None) == Exception
    assert calcula_formula([]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()

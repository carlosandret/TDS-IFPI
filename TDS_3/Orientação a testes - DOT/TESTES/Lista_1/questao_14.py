# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + ½! + 1/3! + 1 /N!

def fatorial(num):
    if not isinstance(num, int) or num < 0:
        return Exception
    valor = 1
    for i in range(num, 0, -1):
        valor *= i
    return valor

def calcula_formula(num):
    if not isinstance(num, int) or num <= 0:
        return Exception

    soma = 1  # inclui o primeiro termo "1" fixo da fórmula
    for i in range(1, num + 1):
        fat = fatorial(i)
        if fat == Exception:
            return Exception
        soma += 1 / fat
    return soma

def main():
    # ACERTOS
    assert round(calcula_formula(1), 2) == round(1 + 1 / 1, 2)
    assert round(calcula_formula(2), 2) == round(1 + 1 / 1 + 1 / 2, 2)
    assert round(calcula_formula(3), 2) == round(1 + 1 / 1 + 1 / 2 + 1 / 6, 2)
    assert round(calcula_formula(5), 2) == round(1 + 1/1 + 1/2 + 1/6 + 1/24 + 1/120, 2)

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


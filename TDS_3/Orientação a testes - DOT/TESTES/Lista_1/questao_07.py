# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def fatorial(num):
    if not isinstance(num, int):
        return Exception
    if num <= 0:
        return Exception
    else:
        valor = 1
        for i in range(num, 0, -1):
            valor *= i
    return valor

def main():
    # ACERTOS
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(5) == 120
    assert fatorial(7) == 5040

    # ERROS
    assert fatorial(0) == Exception
    assert fatorial(-4) == Exception
    assert fatorial("abc") == Exception
    assert fatorial("") == Exception
    assert fatorial(None) == Exception
    assert fatorial(3.5) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()

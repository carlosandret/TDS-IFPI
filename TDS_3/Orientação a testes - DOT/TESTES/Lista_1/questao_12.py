def somatorio(num):
    if not isinstance(num, int) or num <= 0:
        return Exception

    s = 0
    for i in range(1, num + 1):
        s += i
    return s

def main():
    # TESTES VÁLIDOS
    assert somatorio(1) == 1
    assert somatorio(5) == 15
    assert somatorio(10) == 55
    assert somatorio(100) == 5050

    # TESTES INVÁLIDOS
    assert somatorio(0) == Exception
    assert somatorio(-5) == Exception
    assert somatorio("a") == Exception
    assert somatorio(3.5) == Exception
    assert somatorio([1, 2, 3]) == Exception
    assert somatorio(None) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()

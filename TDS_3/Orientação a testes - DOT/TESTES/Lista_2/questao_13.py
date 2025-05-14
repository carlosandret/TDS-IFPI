# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. fazer uma função para gerar os números do dados de forma aleatória

from random import randint

# Função que simula n lançamentos de um dado e conta quantas vezes cada face apareceu
def lancar_dado(n):
    if type(n) != int or n <= 0:
        return Exception

    faces = [0] * 6
    for _ in range(n):
        face = randint(1, 6)
        faces[face - 1] += 1
    return faces

def main():
    # Testes válidos
    resultado = lancar_dado(10)
    assert type(resultado) == list
    assert len(resultado) == 6
    assert sum(resultado) == 10

    resultado = lancar_dado(100)
    assert type(resultado) == list
    assert len(resultado) == 6
    assert sum(resultado) == 100

    # Testes inválidos
    assert lancar_dado(0) == Exception
    assert lancar_dado(-5) == Exception
    assert lancar_dado("dez") == Exception
    assert lancar_dado("") == Exception
    assert lancar_dado(None) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
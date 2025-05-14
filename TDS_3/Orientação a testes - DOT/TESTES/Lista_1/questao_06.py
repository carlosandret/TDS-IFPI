# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

def perimetro(qtd, medida):
    return qtd * medida

def area(medida):
    return medida **2

def calcula_poligono(n_lados, medida):
    if not isinstance(n_lados, int):
        return Exception
    elif not isinstance(medida, (int, float)):
        return Exception
    else:
        if n_lados not in [3, 4, 5] or medida <= 0:
            return Exception
        else:
            if n_lados == 3:
                return "TRIÂNGULO", perimetro(n_lados, medida)
            elif n_lados == 4:
                return "QUADRADO", area(medida)
            else:
                return "PENTAGONO"
            
def main():
    # ACERTOS
    assert calcula_poligono(3, 5) == ("TRIÂNGULO", 15)
    assert calcula_poligono(4, 6) == ("QUADRADO", 36)
    assert calcula_poligono(5, 3) == "PENTAGONO"
    
    # ERROS
    assert calcula_poligono("a", 'B') == Exception
    assert calcula_poligono("", "") == Exception
    assert calcula_poligono(" ", " ") == Exception
    assert calcula_poligono(1.7, 2.5) == Exception
    assert calcula_poligono(7, 9) == Exception
    assert calcula_poligono(-3, 9) == Exception
    
    print("Todos os testes passaram!")

if __name__=="__main__":
    main()

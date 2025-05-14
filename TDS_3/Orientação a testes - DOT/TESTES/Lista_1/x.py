def perimetro(qtd, medida):
    return qtd * medida

def area(medida):
    return medida **2

def calcula_poligono(n_lados, medida):
    # if type(n_lados) != int:
    #     return Exception
    # elif type(medida) != int or type(medida) != float:
    #     return Exception
    # else:
    #     if n_lados not in [3, 4, 5] or medida <= 0:
    #         return Exception
    #     else:
    if n_lados == 3:
        return "TRIÂNGULO", perimetro(n_lados, medida)
    elif n_lados == 4:
        return "QUADRADO", area(medida)
    else:
        return "PENTAGONO!"
    
            
print(calcula_poligono(3, 5))
print(calcula_poligono(4, 6))
print(calcula_poligono(5, 3))
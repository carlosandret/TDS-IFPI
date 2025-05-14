# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área 
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;

def area(raio):
    if type(raio) != float and type(raio) != int:
        return Exception
    
    elif raio > 0:
        return (3.14 * (raio **2))
    
def perimetro(raio):
    if type(raio) != float and type(raio) != int:
        return Exception
    
    if raio > 0:
        return 3.14 * 2 * raio
    
def main():
    # Testes da função area
    assert area(3.5) == 38.465
    assert area(5) == 78.5
    assert area("a") == Exception
    assert area("") == Exception
    assert area(" ") == Exception
    
    # Testes da função perímetro
    assert perimetro(3) == 18.84
    assert perimetro(5.4) == 33.912000000000006
    assert area("a") == Exception
    assert area("") == Exception
    assert area(" ") == Exception

    print("Todos os testes passaram!")

if __name__=="__main__":
    main()
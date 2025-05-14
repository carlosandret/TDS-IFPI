# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar 
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5

def celsius(temp):
    if type(temp) != float and type(temp) != int:
        return Exception
    else:
        return ((temp-32) / 9)*5

def main():
    assert celsius(50) == 10.0
    assert celsius(50.5) == 10.277777777777777
    assert celsius("a") == Exception
    assert celsius("") == Exception
    assert celsius(" ") == Exception
    print("Todos os testes passaram!")
    
if __name__=="__main__":
    main()
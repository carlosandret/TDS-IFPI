def compara(a, b, c):
    if a == b == c:
        resultado = "Todos os valores são iguais"
    elif (a == b and c != a) or (b == c and a != c) or (a == c and b != a):
        resultado = "Existem dois valores iguais e um diferente"
    else:
        resultado = "Todos os valores são diferentes"
    return resultado
def main():
    n1 = int(input(' Digite um número inteiro: '))
    n2 = int(input(' Digite um outro inteiro: '))
    n3 = int(input(' Digite um outro inteiro: '))
    print(compara(n1, n2, n3))
if __name__ == "__main__":
    main()
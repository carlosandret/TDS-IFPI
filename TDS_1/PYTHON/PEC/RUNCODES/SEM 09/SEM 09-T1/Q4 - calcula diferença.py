def diferença(n1, n2, n3):
    resultado = abs(n1 - n3) if abs(n1-n2) > abs(n1 - n3) else abs(n1 - n2)
    return resultado
def main():
    n1 = int(input(' Digite um número inteiro: '))
    n2 = int(input(' Digite outro número inteiro: '))
    n3 = int(input(' Digite outro número inteiro: '))
    print(f'A menor diferença entre os numeros é {diferença(n1, n2, n3)}.')
if __name__ == "__main__":
    main()
def tranforma_anos(ano_t):
    return ano_t * 1//2

def main():
    ano_terrestre = int(input('Digite sua idade: ').strip())
    resultado = tranforma_anos(ano_terrestre)
    print(f"A sua idade em anos espaciais é {resultado}.")
if __name__ == '__main__':
    main()
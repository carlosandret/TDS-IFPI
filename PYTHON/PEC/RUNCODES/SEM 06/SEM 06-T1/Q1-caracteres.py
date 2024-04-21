def comprimento_nome(n):
    return len(n)

def main():
    nome = input("Digite um nome: ").strip()
    quantidade = comprimento_nome(nome)
    print(f'Esse nome possui {quantidade} caraceteres.')

if __name__ == '__main__':
    main()

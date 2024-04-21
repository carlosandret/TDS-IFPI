def mensagem(str):
    if str == '1':
        return 'Ilmo Sr.'
    if str == '2':   
        return 'Ilma Sra.'
    
def main():
    nome = input('Digite o seu nome: ').strip()
    sexo = input('Digite o seu sexo? (1 - masculino ou 2 - feminino): ').strip()
    s = mensagem(sexo)
    print(f'{s} {nome}')  
if __name__ == '__main__':
    main()
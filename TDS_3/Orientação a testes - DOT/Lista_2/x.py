def main():
    try:
        num_posicoes = int(input("\nDigite a quantidade de posições da lista: "))
        lista = []
        
        while True:
            print(f'''\n{'='*10} MENU {'='*10}
1) Cadastrar nome
2) Pesquisar nome
3) Listar todos os nomes
0) Sair do programa''')
            try:
                opcao = int(input("\nDigite sua escolha: "))
                if opcao == 1:
                    nome = input("\nDigite o nome que deseja adicionar: ").strip()
                    if not nome:
                        print("\nERRO: O nome não pode ser vazio!")
                    elif len(lista) >= num_posicoes:
                        print("\nERRO: A lista já alcançou a quantidade máxima!")
                    else:
                        lista.append(nome)
                    
                elif opcao == 2:
                    nome = input("Digite o nome que deseja pesquisar: ").strip()
                    if nome in lista:
                        print(f"\nO nome {nome} ESTÁ na lista, na posição {lista.index(nome)+1}.")
                    else:
                        print(f"\nO nome {nome} NÃO está na lista.")
                elif opcao == 3:
                    if lista:
                        print(f"\nLISTA DE NOMES: {lista}")
                    else:
                        print("\nA lista está vazia.")
                elif opcao == 0:
                    print("\nEncerrando programa...")                
                    break
                else:
                    print("\nERRO: Digite uma opção válida!")
            except ValueError:
                print("\nERRO: Digite um valor numérico válido.")
                
    except ValueError:
        print("\nERRO: Digite um valor numérico válido para a quantidade de posições!")
        main()

if __name__ == "__main__":
    main()

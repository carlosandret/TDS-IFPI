# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.

# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 4) Alterar nome
#  ---> O usuario digita o nome que deseja alterar, mostra a posição do nome e pede o novo nome que será colocado
# 5) Excluir nome
#  ---> Perguntar  se o usuário tem certeza que deseja excluir, sem usar o método remove()
# 0) Sair do programa
# ——————–
# Digite sua escolha:_

# Função que remove o item de uma lista, recebe a lista e o indice do item e retorna a lista com o item removido
def remove_item(lista, indice_item):
    lista_nova = []
    
    lista[indice_item] = ''
    for i in lista:
        if i != '':
            lista_nova.append(i) 
    return lista_nova

def main():    
    num_posicoes = int(input("\nDigite a quantidade de posições da lista de nomes: "))
    if num_posicoes > 0: 
        lista = []
        while True:
            print(f'''\n{'='*10} MENU {'='*10}
1) Cadastrar nome
2) Pesquisar nome
3) Listar todos os nomes
4) Alterar nome
5) Excluir nome
0) Sair do programa''')            
            try:
                opcao = int(input("\nDigite sua escolha: "))
                #  1) Cadastrar nome
                if opcao == 1:
                    nome = input("\nDigite o nome que deseja adicionar: ")
                    # Confere se o valor digitado é composto por letras, tratando caracteres e espaços vasios
                    if nome.isalpha():
                        if len(lista) >= num_posicoes:
                            print("\nERRO: A lista já alcançou a quantidade máxima!")
                        else:
                            lista.append(nome)  
                            print(f"\nO nome {nome} foi adicionado com sucesso!")  
                    else:
                        print("\nERRO: Digite um valor de nome válido!")
                        
                # 2) Pesquisar nome          
                elif opcao == 2:
                    nome = input("\nDigite o nome que deseja pesquisar: ")
                    # Confere se o valor digitado é composto por letras, tratando caracteres e espaços vasios
                    if nome.isalpha():                        
                        if nome in lista:
                            print(f"\nO nome {nome} ESTÁ na lista, na posição {lista.index(nome)+1}.")
                        else:
                            print(f"\nERRO: O nome {nome} NÃO está na lista.")
                    else:
                        print("\nERRO: Digite um valor de nome válido!")
                
                # 3) Mostrar todos os nomes da lista 
                elif opcao == 3:
                    if len(lista) == 0:
                        print("\nA lista está vazia")
                    else:
                        print(f"\nLISTA DE NOMES: {lista}")
                # 4) Alterar nome       
                elif opcao == 4:
                    nome = input("\nDigite o nome que deseja alterar: ")
                    # Confere se o valor digitado é composto por letras, tratando caracteres e espaços vasios
                    if nome.isalpha():                        
                        if nome in lista:
                            print(f"\nO nome {nome} ESTÁ na posição {lista.index(nome)+1}.")
                            novo_nome = input("\nDigite o novo nome: ")
                            lista[lista.index(nome)] = novo_nome
                            print(f"\nO nome {novo_nome} foi adicionado com sucesso!") 
                        else:
                            print(f"\nERRO: O nome {nome} NÃO está na lista. Tente outro nome!")
                    else:
                        print("\nERRO: Digite um valor de nome válido!")
                
                # 5) Excluir nome        
                elif opcao == 5:
                    nome = input("\nDigite o nome que deseja excluir: ")
                    # Confere se o valor digitado é composto por letras, tratando caracteres e espaços vasios
                    if nome.isalpha():
                        if nome in lista:
                            indice_nome = lista.index(nome)
                            print(f"\nO nome {nome} ESTÁ na posição {indice_nome+1}.")
                            opcao = input(f"\nTem certeza que deseja excluir o nome? (S - sim ou N - não) ").lower()
                            if opcao == 's' or opcao == 'sim':         
                                # Chamamento da função que remove o item da lista               
                                lista = remove_item(lista, indice_nome)
                                print(f"\n O nome {nome} foi excluido com sucesso!")
                            elif opcao == 'n' or opcao == 'não':
                                print("\nOK, o nome não será excluido!")
                            else:
                                print("\nERRO: Escolha uma opção válida, S ou N.")
                                
                        else:
                            print(f"\nERRO: O nome {nome} NÃO está na lista. Tente outro nome!")
                    else:
                        print("\nERRO: Digite um valor de nome válido!")
                # 0) Encerrar o programa       
                elif opcao == 0:
                    print("\nEncerrando programa...")                
                    break
            except:
                print("\nERRO: Digite uma opção válida!")    
    else:
        print("\nERRO: A quantidade de posições deve ser um número maior que zero!")            
        main()
if __name__=="__main__":
    main()

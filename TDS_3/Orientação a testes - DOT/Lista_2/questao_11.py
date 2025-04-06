# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.

# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_

def main():
    while True:
        try:
            num_posicoes = int(input("Digite a quantidade de posições da lista: "))
            lista = []
            
            while True:
                print(f'''\n{'='*10} MENU {'='*10}
                \n1) Cadastrar nome
                \n2) Pesquisar nome
                \n3) Listar todos os nomes
                \n0) Sair do programa''')
                opcao = int(input("Digite sua escolha: "))
                if opcao == 1:
                    nome = input("Digite o nome que deseja adicionar: ")
                    if len(lista) <= num_posicoes:
                        lista.append(nome)
                    else:
                        print("ERRO: A lista já alcançou a quantidade máxima!")
                elif opcao == 2:
                    nome = input("Digite o nome que deseja pesquisar: ")
                    for i in lista:
                        if 
                
        except:
            print("ERRO: Digite um valor numérico, tente novamente!")
        

if __name__=="__main__":
    main()

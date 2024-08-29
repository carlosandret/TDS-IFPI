# Escreva um programa Python que apresente o menu de opções abaixo:
# OPÇÕES: 1 - SAUDAÇÃO 2 - BRONCA 3 - FELICITAÇÃO 0 - FIM

# O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:

# 1 - Olá. Como vai? 2 - Vamos estudar mais. 3 - Meus Parabéns! 0 - Fim de serviço.

# Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”. Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando as opções. Obs: use como estrutura de repetição com teste no final e como estrutura condicional múltipla escolha.



def main():
    while True:
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA ")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")

        opcao = int(input(""))
        if opcao == 1:
            print("1 - Olá. Como vai?")
        elif opcao == 2:
            print("2 - Vamos estudar mais.")
        elif opcao == 3:
            print("3 - Meus Parabéns!")
        elif opcao == 0:
            print("0 - Fim de serviço.")
        else:
            print("Opção inválida.")
        if opcao == 0: break
        
if __name__=="__main__":
    main()
 
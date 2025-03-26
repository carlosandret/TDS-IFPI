# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def ler_caractere():
    while True:
        caractere = input("\nDigite um caractere ('S' ou 'N'): ").upper()
        if caractere in ['S', 'N']:
            return caractere
            break
        else:
            print("\nCaractere inválido, digite novamente!")
        
def main():
    while True:
        num = float(input("\nDigite um número: "))
        print(f"\nO cubo de {num} é: {num**3}")
        
        escolha = input("Você quer continuar?('S' ou 'N'): ").upper()
        if escolha == "N":
            break
        elif escolha == "S":
            continue
        else:
            print("\nERRO: Escolha uma opção válida")

    
if __name__=="__main__":
    main()
# Escreva um programa que, para um número indeterminado de pessoas:

# a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag)
# e não deve ser considerada;
# b. calcule e escreva o número de pessoas;
# c. calcule e escreva a idade média do grupo;
# d. calcule e escreva a menor idade e a maior idade.

def calcula_media(total, qtd):
    return total / qtd


def main():
    quantidade_pessoas = 0
    idades = []
    total_idade = 0
    while True:
        print("Digite a sua idade (digite '0' para obter os resultados):", end=" ")
        idade = int(input(""))    
        quantidade_pessoas += 1
        total_idade += idade
        idades.append(idade)
        if idade == 0: break
    idades.remove(0)
    quantidade_pessoas = quantidade_pessoas - 1
    print(f"O número de pessoas é {quantidade_pessoas}")
    print(f"A média das idades é {calcula_media(total_idade, quantidade_pessoas):.2f}")
    print(f"A menor idade é {min(idades)}")
    print(f"A maior idade é {max(idades)}")
    
        
    
if __name__=="__main__":
    main()
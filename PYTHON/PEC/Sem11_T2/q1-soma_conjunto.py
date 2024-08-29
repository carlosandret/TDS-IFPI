# Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação:
# A condição de saída do laço será a leitura do valor 0 (flag).


def main():
    soma = 0
    print("Digite um conjunto de números para obter a soma (pessione '0' para obter o resultado)")
    while True:
        num = int(input(""))
        soma += num
        if num == 0: break
    print(f"O reultado da soma dos números é {soma}.")
    
if __name__=="__main__":
    main()
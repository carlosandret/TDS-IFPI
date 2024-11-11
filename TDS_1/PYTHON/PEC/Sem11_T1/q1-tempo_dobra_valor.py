# Escreva um programa que leia uma quantidade indefinida de números inteiros positivos 
# terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de 
# todos os números lidos (excluindo o zero).

def media(qtd, soma):
    return soma/(qtd -1)

def main():
    print("-" * 100)
    print("Digite os números inteiros que deseja calcular a média (Digite '0' para obter o resultado);")
    print("-" * 100)
    
    quantidade = 0
    soma = 0
    while True:
        num = int(input("Digite: ").strip())
        quantidade += 1
        soma += num
        if num == 0: break
    print(f'A média dos números digitados é {media(quantidade, soma):.2f}')
if __name__ == "__main__":
    main()

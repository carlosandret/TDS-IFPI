# Escreva um programa que leia uma quantidade indefinida de números inteiros positivos 
# terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de 
# todos os números lidos (excluindo o zero).

def media(qtd, soma):
    return soma/(qtd -1)

def main():
    quantidade = 0
    soma = 0
    while True:
        num = int(input("").strip())
        quantidade += 1
        soma += num
        if num == 0: break
    print(f'{media(quantidade, soma):.2f}')
if __name__ == "__main__":
    main()

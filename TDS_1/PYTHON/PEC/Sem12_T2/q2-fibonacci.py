# A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
# subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
# leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
        
        
def main():
    num = int(input("Digite o número de termos que deseja da Sequência de Fibonacci: "))
    termo1 = 0
    termo2 = 1
    print(termo1, end=", ")
    if num > 1:
        print(termo2, end=", ")
        
    for c in range(2, num):
        proximo = termo1 + termo2
        if c == num - 1:
            print(proximo)
        else:
            print(proximo, end=", ")
        termo1 = termo2
        termo2 = proximo
    
if __name__=="__main__":
    main()
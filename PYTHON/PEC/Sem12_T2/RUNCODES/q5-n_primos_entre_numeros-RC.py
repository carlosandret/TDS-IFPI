# Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

def eh_primo(num):
    if num < 2:
        return False
    for c in range(2, int(num ** 0.5) + 1):
        if num % c == 0:
            return False
    return True

def primos_entre(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    
    for num in range(n1, n2 + 1):
        if eh_primo(num):
            print(num)
            
def main():
    n1 = int(input(""))
    n2 = int(input(""))
    
    primos_entre(n1, n2)
    
if __name__=="__main__":
    main()
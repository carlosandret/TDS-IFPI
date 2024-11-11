# Um número é, por definição, primo se ele não tem diorvises, exceto 1 e ele próprio. Escreva um programa
# que leia um número e determine se ele é ou não primo.

def eh_primo(num):
    if num <= 1:
        resultado = False
        
    for c in range(2, int(num**0.5) + 1):
        if num % c == 0:
            resultado = False
    
    resultado = True
    return resultado

def main():
    numero = int(input("Digite um número para saber se ele é primo: "))
    if eh_primo(numero):
        print(True)
    else:
        print(False)
    
if __name__=="__main__":
    main()
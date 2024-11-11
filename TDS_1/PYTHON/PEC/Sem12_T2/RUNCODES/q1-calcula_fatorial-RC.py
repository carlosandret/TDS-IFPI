# Escreva um programa que calcule o fatorial de um número inteiro lido, 
# sabendo-se que:
# N ! = 1 x 2 x 3 x ... x N-1 x N
# 0 ! = 1

def calc_fatorial(num):
    if num == 0:
        resultado = 1
    else:
        resultado = 1
        for c in range(1, num + 1):
            resultado *= c
    return resultado
    
def main():
    numero = int(input(""))
    fatorial = calc_fatorial(numero)
    print(f"{fatorial}") 
if __name__=="__main__":
    main()
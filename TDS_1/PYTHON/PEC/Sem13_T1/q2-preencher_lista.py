# Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com 0 (zero) e imprima a lista;
# b) preencha com os números de 1 a n e imprima a lista;
# c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
# d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
# para sempre incluir os elementos no início da lista;

# Lista de 1 ao número lido
def sequencia_1_a(num):
    lista_sequencia = []
    for c in range(1, num+1):
        lista_sequencia.append(c)
    return lista_sequencia
        
# Lista de números lidos pelo teclado
def ler_numeros(num):
    lista = []
    for c in range(num):
        numero = int(input("Digite valores: "))
        lista.append(numero)
    return lista

# Lista na ordem inversa
def lista_inversa(num):
    lista = []
    for c in range(num):
        numero = int(input("Digite outros valores: "))
        lista.insert(0, numero)
    return lista

def main():
    num = int(input("Digite o número de posições da sua lista: "))
    # Lista com valores 0
    lista_zero = []
    for c in range(num):
        lista_zero.append(0)
        
    lista1 = lista_zero
    lista2 = sequencia_1_a(num)
    lista3 = ler_numeros(num)
    lista4 = lista_inversa(num)
    
    print("Lista preenchida por zeros: ", end="")
    print(f"{lista1}")
    print(f"Sequência de 1 a {num}: ",end='')
    print(f"{lista2}")
    print("Valores lidos pelo teclado: ", end='')
    print(f"{lista3}")
    print("A ordem inversa dos valores lidos é: ", end='')
    print(f"{lista4}")
if __name__=="__main__":
    main()
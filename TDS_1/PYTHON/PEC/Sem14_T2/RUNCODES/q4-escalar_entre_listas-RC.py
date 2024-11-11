# 4. Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o
# produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto
# escalar, sendo que o produto escalar e dado por: (x1 ∗ y1) + (x2 ∗ y2) + (x3 ∗ y3) + ⋯ + (xn ∗ yn).

# Por exemplo, para as duas listas X e Y a seguir:
#     0 1 2 3 4
# X = 2 5 7 3 9
# Y = 3 8 1 0 4
# O produto escalar será: (2 x 3) + (5 x 8) + (7 x 1) + (3 x 0) + (9 x 4) = 89

def recebe_lista(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista

def main():
    lista1 = recebe_lista(5)
    lista2 = recebe_lista(5)
    
    # Imprimir os dois conjuntos e o produto
    # escalar, sendo que o produto escalar e dado por: (x1 ∗ y1) + (x2 ∗ y2) + (x3 ∗ y3) + ⋯ + (xn ∗ yn).
    soma = 0
    for c in range(0, len(lista1)):
        soma += lista1[c] * lista2[c]
        
    print(f"{lista1}")
    print(f"{lista2}")
    print(f"({lista1[0]} x {lista2[0]}) + ({lista1[1]} x {lista2[1]}) + ({lista1[2]} x {lista2[2]}) + ({lista1[3]} x {lista2[3]}) + ({lista1[4]} x {lista2[4]}) = {soma}")

if __name__=="__main__":
    main()
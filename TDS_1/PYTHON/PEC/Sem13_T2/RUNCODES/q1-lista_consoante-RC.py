# 1. Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura
# de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista
# onde cada valor da lista original é a multiplicado pelo valor da constante.
# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e
# o valor da constante e retorna uma nova lista com os elementos multiplicados.

def multiplica_constante(lista, letra):
    lista_resultante = []
    for c in lista:
        lista_resultante.append(c * letra)

    return lista_resultante

def main():
    lista_numeros = []
    while True:
        num = int(input(""))
        if num != 0:            
            lista_numeros.append(num)
        elif num == 0: break
    
    consoante = int(input(""))
    print(f'{multiplica_constante(lista_numeros, consoante)}')
    
    
if __name__=="__main__":
    main()
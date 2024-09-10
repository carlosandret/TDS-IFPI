# Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
# um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos
# anteriores da lista original.
# IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna
# uma lista com a soma cumulativa.

def soma_cumulativa(lista):
    lista_cumulativa = []

    for i in range(0, len(lista)) :
        x = lista[i] + sum(lista[ : i])
        lista_cumulativa.append(round(x))
    return lista_cumulativa

def main():
    lista_numeros = []
    while True:
        num = float(input(""))
        if num != 0:
            lista_numeros.append(num)
        elif num == 0: break
        
    print(f"{soma_cumulativa(lista_numeros)}")
        
if __name__=="__main__":
    main()
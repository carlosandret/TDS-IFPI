#Escreva um programa que leia uma 
# quantidade n, seguido da leitura de #uma lista com n valores. O # programa 
# deve imprimir LISTA ORDENADA ou # LISTA NÃO ORDENADA, conforme o # caso.
# IMPORTANTE: Crie uma função 
# chamada esta_ordenado() que 
# recebe uma lista como parâmetro e 
# retorne True se a lista estiver 
# classificada em ordem crescente, e # False se não for o caso.

def esta_ordenado(lista):
	v = len(lista)
	for c in range(1, v):
		if lista[c-1] > lista[c]:
			return 'LISTA NÃO ORDENADA'
	return 'LISTA ORDENADA'

def ler_valores(num):
    lista_valores = []
    for i in range(num):
        valor = input("").strip()
        if "A" <= valor.upper() < "Z":
            lista_valores.append(ord(valor))
        else:
            lista_valores.append(float(valor))
    return lista_valores

def main():
	qtd = int(input(''))
	valores = ler_valores(qtd)
	print(esta_ordenado(valores))
			

	
	

if __name__ == '__main__':
	main()
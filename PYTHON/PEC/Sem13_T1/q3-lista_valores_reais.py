# 3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
# casas decimais.
# b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
# decimal. Se n = 0, imprima “SEM NOTAS”.
# c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
# Dica: certifique-se de ler apenas um caractere com input()[0]

# Calcula a média dos termos da lista
def calcula_media(lista):
    if len(lista) > 1:
        return sum(lista) / len(lista)
    else:
        return 0 

# Verifica se a letra  é vogal
def eh_vogal(letra):
    return letra in "AEIOUaeiou"

# Recebe as notas em uma lista
def lista_notas(num):
    if num == 0:
        return "SEM NOTAS"
    else:
        print("Digite uma lista de notas:")
        notas = []
        for c in range(num):
            nota = float(input(""))
            nota = f"{nota:.1f}"
            notas.append(float(nota))
        return notas

def main():
    num = int(input("Digite o número de termos da lista: "))
    
    # Lista na ordem inversa de valores reais
    print("Digite uma lista de números: ")
    lista_inversa = []
    for c in range(num):
        numero = float(input(""))
        valor = f'{numero:.4f}'
        valor = str(valor).rstrip("0")
        lista_inversa.insert(0, float(valor))
    
    # Ordem inversa dos valores lidos pelo teclado
    print(f"Valores reais lidos pelo teclado e impressos na ordem inversa: {lista_inversa}")
    
    # Lista de notas e a média
    lista_de_notas = lista_notas(num)  
      
    media_notas = calcula_media(lista_de_notas)
    
    # Lista das notas lidas
    print(f"Lista de notas: {lista_de_notas}")
    # Media das notas lidas
    print(f"A MÉDIA das notas é {media_notas:.1f}")
       
    # c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
    # Dica: certifique-se de ler apenas um caractere com input()[0]
    consoantes = []
    qtd_vogais = 0
    print("Digite algumas letras:")
    for c in range(num):
        letra = input("")[0]
        if eh_vogal(letra):
            qtd_vogais += 1
        else:
            consoantes.append(letra)
    # Quantidade de vogais lidas
    print(f"Existem {qtd_vogais} vogais na lista!")
    # Lista das consoantes lidas
    print(f"Lista de consoantes lidas: {consoantes}")
     
if __name__=="__main__":
    main()
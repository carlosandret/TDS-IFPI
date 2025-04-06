# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

def confere_repeticao(lista, letra):
    cont = 0
    for i in lista:
        if letra == i:
            cont += 1
    return cont

def main():
    while True:
        try:
            l_alfabeto = ['A','A',"A","A","E","Y","T","I","U","O","G","G","G","G","G","D","D"]
            letra = input("\nDigite uma letra do alfabeto: ").upper()
            num_repeticao = confere_repeticao(l_alfabeto, letra)
            print(f"\n{'='*10} Lista: {l_alfabeto} {'='*10}")
            if num_repeticao == 0:
                print(f"\nA letra '{letra}' não está na lista")
            elif num_repeticao == 1:
                print(f"\nA letra '{letra}' se repete {num_repeticao} vez na lista")
            else:
                print(f"\nA letra '{letra}' se repete {num_repeticao} vezes na lista")
            break
        except:
            print("\nERRO: Digite apenas letras, tente novamente!")
if __name__=="__main__":
    main()

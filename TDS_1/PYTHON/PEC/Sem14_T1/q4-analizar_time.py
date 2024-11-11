# 4. Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
# dos jogadores, determine:
# a. o nome e a altura do jogador mais alto;
# b. a média de altura do time;
# c. os jogadores com altura superior à média, listando o nome e a altura de cada um.

def recebe_nome_altura(qtd):
    lista_nomes = []
    lista_alturas = []
    for c in range(qtd):
        nome = input("").strip()
        altura = float(input(""))
        lista_nomes.append(nome)
        lista_alturas.append(altura)
        
    return lista_nomes, lista_alturas

def media_valores_lista(lista):
    return sum(lista) / len(lista)

def main():
    print("Digite uma lista com o nome e altura dos jogadores de um time:")
    lista_nomes, lista_altura = recebe_nome_altura(12)
    
    # O nome e altura do jogador mais alto;
    maior_altura = lista_altura.index(max(lista_altura))
    
    print("JOGADOR MAIS ALTO DO TIME: ")
    print(f"{lista_nomes[maior_altura]}")
    print(f"{max(lista_altura):.2f}")
    
    # A média de altura do time;
    altura_media = media_valores_lista(lista_altura)
    print("ALTURA MÉDIA DO TIME: ", end="")
    print(f"{altura_media:.2f}")
    
    # Os jogadores com altura superior a média, listando o nome e a altura de cada um
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for c in range(0, len(lista_altura)):
        if lista_altura[c] > altura_media:
            print(f"{lista_nomes[c]}")
            print(f"{lista_altura[c]:.2f}")
    
if __name__=="__main__":
    main()
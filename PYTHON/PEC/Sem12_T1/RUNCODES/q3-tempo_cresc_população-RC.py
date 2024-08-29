# Dado um país A, com taxa de natalidade de 2% ao ano, e um país B 
# com uma taxa de natalidade de 3% ano. Sabe-se que, atualmente, 
# o país A tem população maior que o país B. Faça um programa que leia a 
# população de cada país e imprima o tempo necessário para que a população do país B 
# ultrapasse a população do país A.

# A --> 2% por ano
# B --> 3% por ano
# população A > população B

def main():
    p1 = int(input(""))
    p2 = int(input(""))
    if p1 > p2: 
        populacao_a = p1
        populacao_b= p2
    elif p2 > p1: 
        populacao_a = p2
        populacao_b = p1
    
    anos = 0
    while True:
        taxa_n_a =((2 / 100) * populacao_a)
        taxa_n_b =((3 / 100) * populacao_b)
        populacao_a += round(taxa_n_a)
        populacao_b += round(taxa_n_b)
        anos += 1
        if populacao_b > populacao_a: break
    
    # tempo necessário para que a população do país B ultrapasse a população do país A
    print(f"{anos}")
if __name__=="__main__":
    main()

# O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.

# CÓDIGO  PRODUTO         PREÇO (R$)
# H       Hamburger       5.50
# C       Cheeseburger    6.80
# M       Misto Quente    4.50
# A       Americano       7.00
# Q       Queijo Prato    4.00
# X       PARA TOTAL DA CONTA
# Escreva um programa que leia o código e a quantidade de cada item comprado por um freguês, 
# calcule e exiba o total a pagar. Obs: A leitura do código 'X' indica o fim dos itens.

def main():
    total = 0
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")
        codigo = input("").strip().upper()
        # Hamburguer
        if codigo == "H":
            total += 5.5
        # Cheeseburguer
        elif codigo == "C":
            total +=  6.8
        # Misto quente
        elif codigo == "M":
            total +=  4.5
        # Americano
        elif codigo == "A":
            total +=  7
        # Queijo Prato
        elif codigo == "Q":
            total +=  4
                
        if codigo == "X": break
    
    print(f'{total:.2f}')

            
if __name__=="__main__":
    main()
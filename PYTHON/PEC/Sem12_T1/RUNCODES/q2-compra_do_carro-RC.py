# Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro 
# sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, 
# com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.


def main():
    preco_carro = int(input(""))
    poupanca = 10000
    meses = 0
    while True:
        rendimento_p = 0.7/100 * poupanca
        taxa_carro = 0.4/100 * preco_carro
        # Rendimento poupança
        poupanca += rendimento_p
        # preço carro
        preco_carro += taxa_carro
        meses += 1
        if poupanca >= preco_carro: break
        
    print(f"{meses}")
    
if __name__=="__main__":
    main()
    
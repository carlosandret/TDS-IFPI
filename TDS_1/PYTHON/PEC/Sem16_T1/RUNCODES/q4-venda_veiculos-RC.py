# 04.A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em
# mil unidades.

# Fabricante / Ano 2013 2014 2015 2016 2017 2018
# Fiat              204 223  230  257  290  322
# Ford              195 192  198  203  208  228
# GM                220 222  217  231  245  280
# Wolkswagen        254 262  270  284  296  330
# Faça um programa que:
# a) leia os dados da tabela pelo teclado;
# b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
# c) determine e exiba o ano de maior volume geral de vendas.
# d) determine e exiba a média anual de vendas de cada fabricante durante o período.

from random import *

def preenche_matriz(linhas, colunas):
    matriz = []
    for lin in range(linhas):
        linha = []
        for col in range(colunas):
            itens = randint(100, 500) #int(input("").strip())
            linha.append(itens)
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        print("|", end="")
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
            
        print("|")

def main():
    linhas = 4
    colunas = 6
    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

    marcas = {
        0: "Fiat", 1: "Ford", 2: "GM", 3: "Wolkswagen"
    }
    
    ano_indice = {
        2013: 0, 2014: 1, 2015: 2, 2016: 3, 2017: 4, 2018: 5
    }
    indice_ano_veiculo = {
        0: 2013, 1: 2014, 2: 2015, 3: 2016, 4: 2017, 5: 2018 
    }


    
    # As linhas são as marcas de carros
    # As colunas são os anos de referência
    # lin_0 --> Fiat
    # lin_1 --> Ford
    # lin_2 --> GM
    # lin_3 --> Wolkswagen
    
    # Fabricante / Ano 2013 2014 2015 2016 2017 2018
# Fiat              204 223  230  257  290  322
# Ford              195 192  198  203  208  228
# GM                220 222  217  231  245  280
# Wolkswagen        254 262  270  284  296  330

    matriz = preenche_matriz(linhas, colunas)
    
    # b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
    ano = int(input(""))
    
    vendidos_no_ano = []
    for linha in matriz:
       vendidos_no_ano.append(linha[ano_indice[ano]])
    
    indice_ano = vendidos_no_ano.index(max(vendidos_no_ano))
    valor_ano = indice_ano_veiculo(indice_ano)

    imprime_matriz(matriz)
    
    print(vendidos_no_ano)
    print(valor_ano)
    

if __name__=="__main__":
    main()
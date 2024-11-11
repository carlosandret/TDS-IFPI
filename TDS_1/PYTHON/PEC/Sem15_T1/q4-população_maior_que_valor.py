# 04. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
# Veja o exemplo para a leitura de 50000 para a população:
# CIDADES COM MAIS DE 50000 HABITANTES:
# IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
# IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
# IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323
# ...

def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado
        
def main():
    lista_cidades = carrega_cidades()
    populacao = int(input("Digite o valor da população: "))

    # (uf, cod_ibge, nome, dia_aniv, mes_aniv, populacao))
    # dia_nasc_cidades --> [3]
    # mes_nasc_cidades --> [4]
    # nome_cidade --> [2]
    # uf_cidade --> [0]
    # população --> [5]
  

    print(f"CIDADES COM MAIS DE {populacao} HABITANTES:")
    for cidade in lista_cidades:
        if cidade[5] > populacao:
            print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")

if __name__=="__main__":
    main()
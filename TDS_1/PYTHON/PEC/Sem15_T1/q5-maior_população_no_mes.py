# 05. Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês
# informado.
# Veja o exemplo para o mês com valor 4 e 50000 para a população:
# CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:
# Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
# Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril.
# Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril.
# Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril.
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

def nome_meses(num):
    meses_ano = {
        1 : "JANEIRO",
        2 : "FEVEREIRO",
        3 : "MARÇO",
        4 : "ABRIL",
        5 : "MAIO",
        6 : "JUNHO",
        7 : "JULHO",
        8 : "AGOSTO",
        9 : "SETEMBRO",
        10 : "OUTUBRO",
        11 : "NOVEMBRO",
        12 : "DEZEMBRO"
        }
    return meses_ano[num]
        
def main():
    lista_cidades = carrega_cidades()
    print("Digite um mês e uma população: ")
    mes = int(input(""))
    populacao = int(input(""))

    # dia_nasc_cidades --> [3]
    # mes_nasc_cidades --> [4]
    # nome_cidade --> [2]
    # uf_cidade --> [0]

    print(f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {nome_meses(mes)}:")
    
    for cidade in lista_cidades:
        if cidade[5] > populacao:
            if cidade[4] == mes:
                print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {nome_meses(cidade[4]).lower()}.")

if __name__=="__main__":
    main()
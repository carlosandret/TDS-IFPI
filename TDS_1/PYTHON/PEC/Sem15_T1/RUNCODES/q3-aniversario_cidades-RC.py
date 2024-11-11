# 03. Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data.
# Veja o exemplo para o dia 9 e mês 2:
# CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO:
# São Miguel do Passa Quatro(GO)
# Centralina(MG)
# Itaporanga(PB)
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
    dia = int(input(""))
    mes = int(input(""))

    # dia_nasc_cidades --> [3]
    # mes_nasc_cidades --> [4]
    # nome_cidade --> [2]
    # uf_cidade --> [0]

    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {nome_meses(mes)}:")
    
    # Confere se o dia e o mês da cidade são iguais aos vlores lidos
    for cidade in lista_cidades:
        if cidade[3] == dia and cidade[4] == mes:
            print(f"{cidade[2]}({cidade[0]})")
    

if __name__=="__main__":
    main()
    
#cidades = carrega_cidades()
#print(cidades[:3] + cidades[-2:])


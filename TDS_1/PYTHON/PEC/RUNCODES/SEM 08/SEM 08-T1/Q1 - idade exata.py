def calcula_ano(a_atual, a_nasc):
    return a_atual - a_nasc 

def main():
    dia_atual = int(input().strip())
    mes_atual = int(input().strip())
    ano_atual = int(input().strip())
    dia_n = int(input().strip())
    mes_n = int(input().strip())
    ano_n = int(input().strip())
    result_ano = calcula_ano(ano_atual, ano_n)
    if dia_atual < dia_n and mes_atual <= mes_n:
        print(result_ano - 1)
    else:
        print(result_ano)
if __name__ == '__main__':
    main()
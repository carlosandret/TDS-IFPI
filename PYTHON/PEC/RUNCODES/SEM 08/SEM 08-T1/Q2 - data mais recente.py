def menor_data(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'

    elif ano1 == ano2 and mes1 >= mes2 and dia1 >= dia2:
            return f'{dia1}/{mes1}/{ano1}'

    else:
        return f'{dia2}/{mes2}/{ano2}'

def main():
    dia1 = int(input())
    mes1 = int(input())
    ano1 = int(input())
    dia2 = int(input())
    mes2 = int(input())
    ano2 = int(input())
    print(menor_data(dia1, mes1, ano1, dia2, mes2, ano2))

if __name__ == '__main__':
    main()
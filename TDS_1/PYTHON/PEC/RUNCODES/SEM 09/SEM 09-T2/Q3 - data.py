def separa_data(data):
    ano = data % 10000
    data = data // 10000
    mes = data % 100
    dia = data // 100
    return ano, mes, dia

def verifica_ano(ano, mes, dia):
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        if (1000 <= ano <= 9999) and (1 <= mes <= 12):
            if mes == 2:
                return True if (0 < dia <= 29) else False
            elif mes in [1,3,5,7,8,10,12]:
                return True if (0 < dia <= 31) else False
            else:
                return True if (0 < dia <= 30) else False
        else:
            return False

    else:
        if (1000 <= ano <= 9999) and (1 <= mes <= 12): 
            if mes == 2:
                return True if (0 < dia <= 28) else False
        if mes in [1,3,5,7,8,10,12]:
                return True if (0 < dia <= 31) else False
        elif mes in [4,6,9,11]:
           
            return True if (0 < dia <= 30) else False
        else:
            return False
            
def main():
    data = int(input(' Digite uma data no formado DDMMAAA: '))
    ano, mes, dia = separa_data(data)
    print(f'A data é {verifica_ano(ano, mes, dia)}.')
if __name__ == "__main__":
    main()
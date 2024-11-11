# 02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus
# Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as
# temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, ... ).


def nome_mes(mes):
    if mes == 0:
        return 'Janeiro'
    elif mes == 1:
        return 'Fevereiro'
    elif mes == 2:
        return 'Março'
    elif mes == 3:
        return 'Abril'
    elif mes == 4:
        return 'Maio'
    elif mes == 5:
        return 'Junho'
    elif mes == 6:
        return 'Julho'
    elif mes == 7:
        return 'Agosto'
    elif mes == 8:
        return 'Setembro'
    elif mes == 9:
        return 'Outubro'
    elif mes == 10:
        return 'Novembro'
    elif mes ==11:
        return 'Dezembro'
    
# Converter para °K:
def converte_kelvin(temperatura, escala):
    if escala == 'C':
        temperatura = temperatura + 273
    elif escala == 'K':
        temperatura = (temperatura - 32) * 5/9 + 273
    else:
        temperatura = temperatura
    escala='K'
    temp = [temperatura, escala]
    return temp

#Receber a temperatura média de cada mês do ano (°C, °F, ou °K)
def temperatura_mes():
    temperatura_mes = []
    for i in range (12):
        temperatura = float(input())
        escala = input().upper()[0].strip()
        temp_escala = temperatura, escala
        temp_escala = converte_kelvin(temperatura, escala)
        temperatura_mes.append(temp_escala)
    return temperatura_mes

# Calcular a média anual:
def temp_media_anual(temperatura):
    temp_mensal = temperatura
    soma = 0
    for i in range (12):
        temperatura = temp_mensal[i][0]
        soma += temperatura
    media = soma/12
    return f'{media:.2f}'

# Retornar as temperaturas maiores que a média anual e respectivo mês:
def temp_maior_que_media(media, mes, temperatura):
    if temperatura[mes][0] > media:
        mes = nome_mes(mes)
        meses_mais_quentes = (f'{mes}: {temperatura[mes][0]:.2f}K')
    return meses_mais_quentes

def main():
    temperatura = temperatura_mes()
    print ("TEMPERATURA MÉDIA ANUAL")
    media = temp_media_anual(temperatura)
    print (f'{media}K')
    print ("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    for mes in range (12):
        meses_quentes=temp_maior_que_media(media, mes,temperatura)
        print(meses_quentes)

if __name__=='__main__':
    main()
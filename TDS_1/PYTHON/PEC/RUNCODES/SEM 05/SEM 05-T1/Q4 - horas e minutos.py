def t_hora (minutos):
    m = minutos // 60
    return m
def t_minuto(minutos):
    h = minutos % 60
    return h
def main():
    min = int(input('Digite a quantidade de minutos: ').strip())

    horas = t_hora(min)
    minuto = t_minuto(min)

    print(f'Esse valor corresponde em horas e minutos a {horas}:{minuto}.')


if __name__ == '__main__':
    main()

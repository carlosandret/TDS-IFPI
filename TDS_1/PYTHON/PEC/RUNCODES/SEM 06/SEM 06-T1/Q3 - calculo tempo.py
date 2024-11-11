def calcula_tempo(time):
    hora = time // 3600
    seg_total = time % 3600
    min = seg_total // 60
    seg = seg_total % 60
    return f'{hora}:{min}:{seg}'

def main():
    t_segundos = int(input('Digite o tempo de duração de um evento em uma fábrica em segundos: ').strip())
    tempo = calcula_tempo(t_segundos)
    print(f"Esse tempo corresponde a {tempo}.")

if __name__ == '__main__':
    main()
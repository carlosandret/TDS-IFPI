def semaforo(str):
    if str.upper() == 'V':
        return 'Siga'
    if str.upper() == 'A':
        return 'Atenção'
    if str.upper() == 'E':
        return 'Pare'
    
def main():
    cor = input('Qual a cor do sinal de trânsito? (“V” é verde; “A" amarelo; “E” é vermelho): ').strip()
    resultado = semaforo(cor)
    print(f'{resultado}')
if __name__ == '__main__':
    main()
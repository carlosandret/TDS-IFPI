def ler_signos(d, m):
    if m == 2 and 19 <= d <= 30 or m == 3 and 1 <= d <= 20: 
        return 'Peixes'
    
    if m == 3 and 21 <= d <= 30 or m == 4 and 1 <= d <= 19: 
        return 'Áries'
    
    if m == 4 and 20 <= d <= 30 or m == 5 and 1 <= d <= 20:
        return 'Touro'
    
    if m == 5 and 21 <= d <= 30 or m == 6 and 1 <= d <= 21: 
        return 'Gêmeos'
    
    if m == 6 and 22 <= d <= 30 or m == 7 and 1 <= d <= 22:
        return 'Câncer'
    
    if m == 7 and 23 <= d <= 30 or m == 8 and 1 <= d <= 22:
        return 'Leão'
    
    if m == 8 and 23 <= d <= 30 or m == 9 and 1 <= d <= 22:
        return 'Virgem'
    
    if m == 9 and 23 <= d <= 30 or m == 10 and 1 <= d <= 22: 
        return 'Libra'
    
    if m == 10 and 23 <= d <= 30 or m == 11 and 1 <= d <= 21:
        return 'Escorpião'
    
    if m == 11 and 22 <= d <= 30 or m == 12 and 1 <= d <= 21:
        return 'Sagitário'
    
    if m == 12 and 22 <= d <= 30 or m == 1 and 1 <= d <= 19:
        return 'Capricórnio'
    
    if m == 1 and 20 <= d <= 30 or m == 2 and 1 <= d <= 18: 
        return 'Aquário'  
    
def main():
    data = int(input('Digite o dia em que voçẽ nasceu: ').strip())
    mes = int(input('Digite o mês em que voçẽ nasceu: ').strip())
    print(f'O seu signo é {ler_signos(data, mes)}.')

if __name__ == '__main__':
    main()
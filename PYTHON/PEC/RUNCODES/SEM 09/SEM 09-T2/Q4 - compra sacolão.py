def valor_total(maca, mor):
    #valor total morango
    v_mor = mor * 2.50 if mor <= 5 else mor * 2.20
    v_maca = maca * 1.80 if maca <= 5 else maca * 1.50
    return v_mor + v_maca

def main():
    morango = float(input(' Digite a quantidade (em Kg) de morangos: '))
    maca = float(input(' a quantidade (em Kg) de maças: '))
    q_total = morango + maca
    valor = valor_total(maca, morango)
    if q_total > 8 or valor > 25:
        valor -= (valor * 10/100)
    print(f'O valor a ser pago É {valor:.2f}.') 
if __name__ == "__main__":
    main()
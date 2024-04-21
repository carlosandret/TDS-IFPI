def calc_quantidade(a, b, c, d, e):
    t = 0
    if a == 'S':
        t += 1
    if b == 'S':
        t += 1
    if c == 'S':
        t += 1
    if d == 'S':
        t += 1
    if e == 'S':
        t += 1
    return t

def main():
    p1 = input('Telefonou para a vítima? ').upper().strip()
    p2 = input("Esteve no local do crime? ").upper().strip()
    p3 = input("Mora perto da vítima ? ").upper().strip()
    p4 = input("Devia para a vítima ? ").upper().strip()
    p5 = input("Já trabalhou com a vítima ? ").upper().strip()
    print('O interrogado é: ')
    total = calc_quantidade(p1, p2, p3, p4, p5)
    if total == 2:
        print('Suspeito')
    elif total == 3 or total == 4:
        print('Cúmplice')
    elif total == 5:
        print('Assassino')
    else:
        print('Inocente')
if __name__ == "__main__":
    main()
def q_caractere(str, nom1):
    if str == '1':
        nom2 = input('').strip()
        resultado = len(nom1) + len(nom2)
        return resultado
    if str == '2':
        r = len(nom1)
        return r
def main():
    nome = input('').strip()
    e_civil = input('').strip()
    resultado = q_caractere(e_civil, nome)
    print(resultado)
if __name__ == '__main__':
    main()
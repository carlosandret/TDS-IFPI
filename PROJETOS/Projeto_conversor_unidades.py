def separa_numero(num):
    num = int(num)
    n1 = num % 10
    num //= 10
    n2 = num % 10
    num //= 10
    n3 = num % 10
    num //= 10
    n4 = num % 10
    num //= 10
    n5 = num % 10
    num //= 10
    n6 = num % 10
    num //= 10
    n7 = num % 10
    num //= 10
    n8 = num % 10
    num //= 10
    n9 = num % 10
    num //= 10
    n10 = num % 10
    num //= 10
    n11 = num % 10
    num //= 10
    n12 = num % 10
    num //= 10
    n13 = num % 10
    num //= 10
    n14 = num % 10
    num //= 10
    n15 = num % 10
    num //= 10
    n16 = num // 10
    return n16, n15, n14, n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1

def binario_decimal(num):
    num = int(num)
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16 = separa_numero(num)
    v1 = n16 * 2 ** 0
    v2 = n15 * 2 ** 1
    v3 = n14 * 2 ** 2
    v4 = n13 * 2 ** 3
    v5 = n12 * 2 ** 4
    v6 = n11 * 2 ** 5
    v7 = n10 * 2 ** 6
    v8 = n9 * 2 ** 7
    v9 = n8 * 2 ** 8
    v10 = n7 * 2 ** 9
    v11 = n6 * 2 ** 10
    v12 = n5 * 2 ** 11
    v13 = n4 * 2 ** 12
    v14 = n3 * 2 ** 13
    v15 = n2 * 2 ** 14
    v16 = n1 * 2 ** 15

    return v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10 + v11 + v12 + v13 + v14 + v15 + v16

def decimal_binario(num):
    num = int(num)
    v16 = num % 2
    num //= 2
    v15 = num % 2
    num //= 2
    v14 = num % 2
    num //= 2
    v13 = num % 2
    num //= 2
    v12 = num % 2
    num //= 2
    v11 = num % 2
    num //= 2
    v10 = num % 2
    num //= 2
    v9 = num % 2
    num //= 2
    v8 = num % 2
    num //= 2
    v7 = num % 2
    num //= 2
    v6 = num % 2
    num //= 2
    v5 = num % 2
    num //= 2
    v4 = num % 2
    num //= 2
    v3 = num % 2
    num //= 2
    v2 = num % 2
    v1 = num // 2
    return str(v1) + str(v2) + str(v3) + str(v4) + str(v5) + str(v6) + str(v7) + str(v8) + str(v9) + str(v10) + str(v11) + str(v12) + str(v13) + str(v14) + str(v15) + str(v16)
    
def decimal_octal(num):
    num = int(num)
    v6 = num % 8
    num //= 8
    v5 = num % 8
    num //= 8
    v4 = num % 8
    num //= 8
    v3 = num % 8
    num //= 8
    v2 = num % 8
    v1 = num // 8
    return v6 + (v5 * 10) + (v4 * 100) + (v3 * 1000) + (v2 * 10000) + (v1 * 100000)

def octal_decimal(num):
    num = int(num)
    n1, n2, n3, n4, n5, n6, n7, n8 = separa_numero(num)
    v1 = n8 * 8 ** 0
    v2 = n7 * 8 ** 1
    v3 = n6 * 8 ** 2
    v4 = n5 * 8 ** 3
    v5 = n4 * 8 ** 4
    v6 = n3 * 8 ** 5
    v7 = n2 * 8 ** 6
    v8 = n1 * 8 ** 7
    return v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8

def octal_binario(num):
    valor = octal_decimal(num)
    return decimal_binario(valor)

def binario_octal(num):
    valor = binario_decimal(num)
    return decimal_octal(valor)

def decimal_hexadecimal(num):
    num = int(num)
    hexa_ = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    v6 = num % 16
    num //= 16
    v5 = num % 16
    num //= 16
    v4 = num % 16
    num //= 16
    v3 = num % 16
    num //= 16
    v2 = num % 16
    v1 = num // 16
    
    if v6 in [10, 11, 12, 13, 14, 15]:
        v6 = hexa_[v6]
    if v5 in [10, 11, 12, 13, 14, 15]:
        v5 = hexa_[v5]
    if v4 in [10, 11, 12, 13, 14, 15]:
        v4 = hexa_[v4]
    if v3 in [10, 11, 12, 13, 14, 15]:
        v3 = hexa_[v3]
    if v2 in [10, 11, 12, 13, 14, 15]:
        v2 = hexa_[v2]
    if v1 in [10, 11, 12, 13, 14, 15]:
        v1 = hexa_[v1]
    
    r = str(v1)+ str(v2) + str(v3) + str(v4) + str(v5) + str(v6)
    return (r.lstrip('0'))

def hexadecimal_decimal(num):
    num = str(num)
    return int(num, 16)

def hexadecimal_binario(num):
    num = hexadecimal_decimal(num)
    return decimal_binario(num)

def hexadecimal_octal(num):
    num = hexadecimal_decimal(num)
    return decimal_octal(num)

def binario_hexadecimal(num):
    num = binario_decimal(num)
    return decimal_hexadecimal(num)

def octal_hexadecimal(num):
    num = octal_decimal(num)
    return decimal_hexadecimal(num)

def main():
    print("\033[1;92m", '<-------- CONVERSOR DE UNDADES -------->', "\033[m")
    base_entrada = input('''Selecione qual a base do seu número:
        (1)-Decimal
        (2)-Binário
        (3)-Octal
        (4)-Hexadecimal
            ''')

    base_saida = input('''Selecione qual a base do número que deseja transformar:
        (1)-Decimal
        (2)-Binário
        (3)-Octal
        [4]-Hexadecimal
            ''')
    numero = input(" Digite o número: ")
     
        # Decimal --> binário 
    if base_entrada == "1" and base_saida == "2":
        resultado = decimal_binario(numero)
        print(f"O número {numero} em Binário é {resultado}.")
        # Decimal --> octal 
    elif base_entrada == "1" and base_saida == "3":
        resultado = decimal_octal(numero)
        print(f"O número {numero} em Octal é {resultado}.")
        # Decimal --> hexadecimal
    elif base_entrada == "1" and base_saida == "4":
        resultado = decimal_hexadecimal(numero)
        print(f'O número {numero} em Hexadecimal é {resultado}')
        
        # Octal --> decimal 
    elif base_entrada == "3" and base_saida == "1":
        resultado = octal_decimal(numero)
        print(f"O número {numero} em Decimal é {resultado}.")
        # Octal --> binário
    elif base_entrada == "3" and base_saida == "2":
        resultado = octal_binario(numero)
        print(f'O número {numero} em Binário é {resultado}')
        # Octal --> binário
    elif base_entrada == "3" and base_saida == "4":
        resultado = octal_hexadecimal(numero)
        print(f'O número {numero} em Hexadecimal é {resultado}')
        
        # Binário -->  decimal
    elif base_entrada == "2" and base_saida == "1":
        resultado = binario_decimal(numero)
        print(f"O número {numero} em Decimal é {resultado}.")
        # Binário --> octal
    elif base_entrada == "2" and base_saida == "3":
        resultado = binario_octal(numero)
        print(f'O número {numero} em Octal é {resultado}')
        # Binário --> hexadecimal
    elif base_entrada == "2" and base_saida == "4":
        resultado = binario_hexadecimal(numero)
        print(f'O número {numero} em Hexadecimal é {resultado}')
        
        # Hexadecimal --> Decimal
    elif base_entrada == "4" and base_saida == "1":
        resultado = hexadecimal_decimal(numero)
        print(f'O número {numero} em Decimal é {resultado}')
        # Hexadecimal --> binário
    elif base_entrada == "4" and base_saida == "2":
        resultado = hexadecimal_binario(numero)
        print(f"O número {numero} em Binário é {resultado}")
        # Hexadecimal --> octal
    elif base_entrada == "4" and base_saida == "3":
        resultado = hexadecimal_octal(numero)
        print(f"O número {numero} em Octal é {resultado}")

if __name__ == "__main__":
    main()

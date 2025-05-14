# 1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def confere_par(n):
    if type(n) == int:
        if n % 2 == 0:
            return True
        elif n % 3 == 0:
            return False
    else:
        return Exception

def main():
    assert confere_par(4) == True
    assert confere_par(3) == False
    assert confere_par(-3) == False
    assert confere_par('e') == Exception
    assert confere_par(3.5) == Exception
    print("Todos os testes passaram!")
    
if __name__=="__main__":
    main()
    
    

# def main():
#     while True:
#         try:
#             num = int(input("\nDigite um número: "))
#             if confere_par(num) == True:
#                 print(f"\nO número {num} é par")
#             else:
#                 print(f"\nO número {num} é ímpar")
#                 break
#         except:
#             print("ERRO: Digite um número válido!!")

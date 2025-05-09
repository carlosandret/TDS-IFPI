# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

def calcula_formula(num):
    soma = 0
    for i in range(1, num+1):
        soma += 1/i
    return soma
    
def main():
    while True:
        try:
            numero = int(input("\nDigite um número: "))
            if numero > 0:    
                print(f"\nO resultado da formula [1 + ½ + 1/3 + ¼ + 1/5 ... 1/N] com o número {numero} é: {calcula_formula(numero):.2f}")
                break
            else:
                print("\nERRO: O número deve ser positivo e diferente de zero!")
        except:
            print("\nERRO: Entrada inválida, digite somente valores numéricos!")

if __name__=="__main__":
    main()
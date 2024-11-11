# Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.” 
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
# Após informar uma nota válida, o aluno deve ver seu conceito, segundo a tabela:

# Conceito	Nota
# A	>= 8,5
# B	>= 7,0
# c	>= 5,0
# D	>= 4,0
# E	>= 0,0

def main():
    while True:
        nota = float(input("Digite a sua nota (entre 0 e 10): ").strip())
        if nota not in range(0, 11):
            print("Nota inválida.")
        elif 0 <= nota < 4 :
            print("Conceito:", end=" ")
            print("E")
            break
        elif 4 <= nota < 5:
            print("Conceito:", end=" ")
            print("D")
            break
        elif 5 <= nota < 7:
            print("Conceito:", end=" ")
            print("C")
            break
        elif 7 <= nota < 8.5:
            print("Conceito:", end=" ")
            print("B")
            break
        elif 8.5 <= nota <= 10:
            print("Conceito:", end=" ")
            print("A")
            break
         
if __name__ == "__main__":
    main()
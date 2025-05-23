# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas 
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno 
# foi aprovado (considere 6.0 a média mínima para aprovação).

def media(n1, n2):
    if type(n1) != float and type(n2) != int:
        return Exception
    else:
        return (n1+n2) / 2

def main():
    assert media(5, 6) == 5.5
    assert media(3.5, 8.9) == 6.2
    assert media("a", 'B') == Exception
    assert media("", "") == Exception
    assert media(" ", " ") == Exception
    
    print("Todos os testes passaram!")
    
if __name__=="__main__":
    main()


# def main():
#     while True:
#         try:
#             n1 = float(input("Digite a primeira nota: "))
#             n2 = float(input("Digite a segunda nota: "))
#             valor_media = media(n1, n2)
#             print(f"Sua média do semestre foi: {valor_media}")
#             if valor_media >= 6:
#                 print(f"você foi aprovado, PARABENS!")
#             else:
#                 print("Você foi reprovado!")
#             break
#         except:
#             print("\nERRO: Nota inválida, digite novamente!")
# if __name__=="__main__":
#     main()
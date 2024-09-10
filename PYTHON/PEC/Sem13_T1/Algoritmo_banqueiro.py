from random import *
# C --> Matriz de recurso que está sendo usado
# R --> Matriz requisições
# E --> Recursos Totais
# A --> Recursos disponiveis

def soma_linhas(lc, l2):
    return [x + y for x, y in zip(lc, l2)]

def main():
    numeros = []
    for c in range(32):
        x = randint(0, 9)
        numeros.append(x)
    L1 = numeros[:4]
    numeros = numeros[4:]
    L2 = numeros[:4]
    numeros = numeros[4:]
    L3 = numeros[:4]
    numeros = numeros[4:]
    L4 = numeros[:4]
    numeros = numeros[4:]
    L5 = numeros[:4]
    numeros = numeros[4:]
    L6 = numeros[:4]
    numeros = numeros[4:]
    L7 = numeros[:4]
    numeros = numeros[4:]
    L8 = numeros[:4]
    
    # Estabelecendo parâmetros
    C = [
        L1,#--> P1
        L2, #--> P2
        L3 #--> P3
    ]
    R = [
        L4, #--> P1
        L5, #--> P2
        L6 #--> P3
    ]
    E = L7
    A = L8

    print('<',"-"*10, end=' ')
    print('ALGORITMO DO BANCÁRIO', end=' ')
    print("-"*10,">")
    print("\n")
    # Conferir se a linha  R é menor ou igual à linha A
    for i in range(2, -1, -1):
        l1 = R[i]
        linha_corrente = C[i]
        l2 = A
        if l1[0] <= l2[0] and l1[1] <= l2[1] and l1[2] <= l2[2] :
                # Se a condição for verdadeira os recursos disponíveis irão somar com os que estavm sendo utilizados
                A = soma_linhas(linha_corrente, l2)
                if i == 0:
                    p_seguro = 'P1'
                elif i == 1:
                    p_seguro = 'P2'
                elif i == 2:
                    p_seguro = 'P3'
                print(f"O processo {p_seguro} é seguro!!")
        else:
            if i == 0:
                processo_deadlock = "P1"
            elif i == 1:
                processo_deadlock = "P2"
            elif i == 2:
                processo_deadlock = "P3"
            print(f"A linha {l1} do processo {processo_deadlock} está em deadlock")    

    print(f"Quantidade recursos Disponíveis (A): {A}")
    print(f"Total de recursos do sistema (E): {E}")    
    print("\033[1;92m", '\nO sistema é completamente seguro!!', "\033[m") if A >= E else print("\033[1;31m",'\nO programa não é seguro!!', "\033[m")
    
if __name__=="__main__":
    main()
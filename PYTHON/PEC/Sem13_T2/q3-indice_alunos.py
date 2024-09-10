# 3. Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que
# tem nota maior ou igual a 6 (seis).



def main():
    notas_alunos = []
    print("Digite a nota de 50 alunos:")
    for i in range(50):
        nota = float(input(""))
        notas_alunos.append(nota)
    
    lista_final = []
    for i in range(0, len(notas_alunos)):
        if notas_alunos[i] >= 6:
            lista_final.append(i)
        else:
            continue
    
    print(f"Os índices das notas maiores ou igual a 6 são: {lista_final}")
    
if __name__=="__main__":
    main()
# O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha
# Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6%
# dos animais vivos no começo do ano morreram e o número de
# animais nascidos ao longo do ano que sobreviveram foi de 1% da população
# inicial.
# Escreva um programa que leia a população de aves no início do ano 1600 e
# imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população
# por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução
# quanto a população total cai para menos de 10% da população original.

def main():
    populacao_original = populacao = int(input("Digite a população de Dodôs no início do ano 1600: ").strip())
    # 6% dos vivos morrem e 1% da populacao inicial nasce
    ano = 1599
    while True:
        num_nascimento = (1 / 100) * populacao
        num_mortes = (6 / 100) * populacao
        total_ano = (num_nascimento + populacao) - num_mortes
        ano += 1
        populacao = total_ano
        if total_ano < ((10 /100) * populacao_original): break
        
    print("anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano é:")
    print(f"{ano},{round(num_nascimento)},{round(num_mortes)},{round(total_ano)}".strip())
    
if __name__=="__main__":
    main()
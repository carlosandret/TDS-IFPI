# 5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais
# alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
# altura arredondando para duas casas decimais.

def recebe_lista_alunos(qtd):
    lista_nome = []
    lista_idade = []
    lista_altura = []
    for c in range(qtd):
        nome = input("").strip()
        idade = int(input(""))
        altura = float(input(""))
        lista_nome.append(nome)
        lista_idade.append(idade)
        lista_altura.append(round(altura, 2))
    return lista_nome, lista_idade, lista_altura

def media_valores_lista(lista):
    return sum(lista) / len(lista)

# quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
# altura arredondando para duas casas decimais.

def main():
    nome, idade, altura = recebe_lista_alunos(30)
    
    media_altura = media_valores_lista(altura)
    
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for c in range(0, len(idade)):
        if idade[c] > 13 and round(altura[c], 2) < round(media_altura, 2):
            print(f"{nome[c]}")
        else:
            continue
    
if __name__=="__main__":
    main()
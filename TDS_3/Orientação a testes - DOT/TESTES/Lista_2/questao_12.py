# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas. 

# Função que gera uma lista aleatória de respostas de "A" a "E", com tamanho determinado ao chamar a função, retornando ao final a lista criada
import random

# Função que gera uma lista aleatória de respostas de "A" a "E"
def gera_respostas(num_questoes):
    if not isinstance(num_questoes, int) or num_questoes <= 0:
        return Exception

    alternativas = ["A", "B", "C", "D", "E"]
    lista = [random.choice(alternativas) for _ in range(num_questoes)]
    return lista

# Função que calcula os acertos de um aluno comparando com o gabarito
def corrige_prova(gabarito, respostas):
    if not isinstance(gabarito, list) or not isinstance(respostas, list):
        return Exception
    if len(gabarito) != len(respostas):
        return Exception
    if not all(isinstance(r, str) and r in "ABCDE" for r in respostas + gabarito):
        return Exception

    return sum(1 for i in range(len(gabarito)) if respostas[i] == gabarito[i])

def main():
    gabarito = ["A", "B", "C", "D", "E"] * 6  # 30 questões
    aluno1 = ["A", "B", "C", "D", "E"] * 6          # 30 acertos
    aluno2 = ["E", "D", "C", "B", "A"] * 6          # 6 acertos

    # Testes válidos
    assert gera_respostas(5).__len__() == 5
    assert corrige_prova(gabarito, aluno1) == 30
    assert corrige_prova(gabarito, aluno2) == 6

    # Testes inválidos para gera_respostas
    assert gera_respostas("dez") == Exception
    assert gera_respostas(-5) == Exception

    # Testes inválidos para corrige_prova
    assert corrige_prova("A", aluno1) == Exception
    assert corrige_prova(gabarito, "B") == Exception
    assert corrige_prova(gabarito, ["A", "B", "C"]) == Exception  # tamanho diferente
    assert corrige_prova(gabarito, ["A"] * 29 + [9]) == Exception  # item não string

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
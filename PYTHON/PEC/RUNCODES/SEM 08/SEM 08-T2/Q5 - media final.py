def calcula_media(nota1, nota2, nota3, media):
    return (nota1 + nota2 * 2 + nota3 * 3 + media) / 7

def mede_conceito(media_final):
    if media_final < 4.0:
        conceito = 'E\nReprovado'
    elif media_final >= 4.0 and media_final < 6.0:
        conceito = 'D\nReprovado'
    elif media_final >= 6.0 and media_final < 7.5:
        conceito = 'C\nAprovado'
    elif media_final >= 7.5 and media_final < 9.0:
        conceito = 'B\nAprovado'
    else:
        conceito = 'A\nAprovado'
    return conceito
   
def main():
    matricula = input(' Digite a sua matrícula: ').strip()
    print(' Digite suas três notas das provas: ')
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media = float(input(' Digite a média das notas: '))
    media_final = calcula_media(nota1, nota2, nota3, media)
    conceito = mede_conceito(media_final)
    print(matricula)
    print(f'Sua média final é {media_final:.2f}.')
    print(conceito)
if __name__ == '__main__':
    main()
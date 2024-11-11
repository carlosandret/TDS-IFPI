altura = int(input('Digite a altura: ').strip())
comprimento = int(input('Digite o comprimento: ').strip())
largura = int(input('Digite a largura: ').strip())
area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_paredes = 2 * altura * largura + 2 * altura * comprimento
print(f'A área do piso da sala é {area_piso}.')
print(f'O volume da sala é {volume_sala}.')
print(f'A área das paredes da sala é {area_paredes}.')
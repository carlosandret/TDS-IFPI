print('Quantas porções de cada ingrediente são necessárias para a poção que você está preparando? ')
pó_de_lua= int(input('Pó de Lua Estelar: ').strip())
Essência_de_Dragão = int(input('Essência de Dragão: ').strip())
Lágrimas_de_Fênix = int(input('Lágrimas de Fênix: ').strip())
preço1 = pó_de_lua * 5
preço2 = Essência_de_Dragão * 3
preço3 = Lágrimas_de_Fênix * 8
print('O custo total será:',preço1 + preço2 + preço3,'moedas de ouro')

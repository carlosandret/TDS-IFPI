alfabeto = "abcdefghijclmnopqrstuvwxyz"

chave = 3

letra = input("Por favor, entre com uma letra para criptografar: ")

posicao = alfabeto.find(letra)

novaPosicao = (posicao + chave) % 26

letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é", letraCriptografada)
alfabeto = "abcdefghijclmnopqrstuvwxyz"

mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

mensagemCriptografada = ''

chave = int(input("Por favor, entre com a chave: "))

for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)
        novaPosicao = (posicao + chave) % 26
        mensagemCriptografada += alfabeto[novaPosicao]
        
    else:
        mensagemCriptografada += char

print("Sua mensagem criptografada é: ", mensagemCriptografada)    
        
        

alfabeto = "cdkevfghjlmanbwoiqrstpuxyz"
opcao = int(input('''
Escolha se quer criptografar ou descriptografar:
[ 1 ] CRIPTOGRAFAR
[ 2 ] DESCRIPTOGRAFAR
    \n
'''))

# Criptografa a mensagem do usuário
if opcao == 1:
    mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()
    mensagemCriptografada = ''

    for char in mensagem:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            chave = int(input("Por favor, entre com a chave: "))
            novaPosicao = (posicao + chave) % 26
            mensagemCriptografada += alfabeto[novaPosicao]


    print("Sua mensagem criptografada é: ", mensagemCriptografada.upper())    

# Descriptografa a mensagem do usuário
elif opcao == 2:
    mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()
    mensagemDescriptografada = ''

    for char in mensagem:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            chave = int(input("Por favor, entre com a chave: "))
            novaPosicao = (posicao + chave) % 26
            mensagemDescriptografada += alfabeto[novaPosicao]
            
        else:
            mensagemDescriptografada += char

    print("Sua mensagem criptografada é: ", mensagemDescriptografada.upper())    
        
else:
    print("Esta opção é inválida, tente novamente!!!")
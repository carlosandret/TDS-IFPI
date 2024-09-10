alfabeto = "abcdefghijclmnopqrstuvwxyz"
opcao = int(input('''
Escolha se quer criptografar ou descriptografar:
[ 1 ] CRIPTOGRAFAR
[ 2 ] DESCRIPTOGRAFAR
    \n
'''))

if opcao == 1:    
    mensagem = input("Por favor, entre com as letras para criptografar: ").lower()
    chave = int(input("Digite a chave para criptrografar: "))
    letras = list(mensagem)
    mensagemCriptografada = []
    for i in letras:
        posicao = alfabeto.find(i)
        novaPosicao = (posicao + chave) % 26
        mensagemCriptografada.append(alfabeto[novaPosicao]) 
    print(f"Sua letra criptografada é [ {''.join(mensagemCriptografada)} ]")
    
elif opcao == 2:
    mensagem = input("Por favor, entre com as letras para descriptografar: ").lower()
    chave = int(input("Digite a chave para descriptrografar: "))
    letras = list(mensagem)
    mensagemDescriptografada = []
    for i in letras:
        posicao = alfabeto.find(i)
        novaPosicao = (posicao + chave) % 26
        mensagemDescriptografada.append(alfabeto[novaPosicao]) 
    print(f"Sua letra criptografada é [ {''.join(mensagemDescriptografada)} ]")

else:
    print("Esta opção é inválida, tente novamente!!!")
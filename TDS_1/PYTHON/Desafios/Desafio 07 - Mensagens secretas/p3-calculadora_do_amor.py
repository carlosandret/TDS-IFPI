print("Calculadora do Amor")
print("<3 " * 8)

nome1 = input("Digite o seu nome: ")
nome2 = input("Digite o nome do(a) parceiro(a): ")

placar = 0
for i in list(nome1):
    if i.lower() in "aeiou":
        placar += 5
    elif i.lower() in "amor":
        placar += 10

print("Seu placar de compatibilidade : ", placar)
        
if placar < 10:
    print("Esqueça esta pesoa! Nunca vai dar certo!")
    
else:
    print("Vocês terão um relacionamento muito intenso! <3")
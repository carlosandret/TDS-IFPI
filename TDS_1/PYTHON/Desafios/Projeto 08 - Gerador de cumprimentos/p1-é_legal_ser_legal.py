from random import *

print("Gerador de Cumprimentos")
print("-" * 21)

adjetivos = ["maravilhoso", "acima da media", "excelente"]

hobbies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual  seu nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")
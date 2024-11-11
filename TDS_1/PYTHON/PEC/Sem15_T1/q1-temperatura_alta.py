# 01. Considereuma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes:
# temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é
# representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as
# temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de
# duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4
# (quatro) casas decimais).
# Use upper() e colchetes [] para garantir a leitura correta da escala com apenas um caractere, por exemplo:
# escala = input('Escala : ').upper()[0]
# As fórmulas, a seguir, mostram como realizar a conversão entre as escalas solicitadas::
# °F = (°C * (9/5)) + 32 | °C = (°F - 32) * (5/9)

def converte_para_celsius(F):
    temperatura_celsius = (F - 32) * (5/9)
    return temperatura_celsius

def converte_para_fahrenheit(C):
    temperatura_fahrenheit = (C * (9/5)) + 32
    return temperatura_fahrenheit

def altera_escala(t1, t2):
    valor1 = t1[0]
    valor2 = t2[0]
    
    if t1[1] != t2[1]:
        if t1[1] == "C":
            valor2 = converte_para_celsius(valor2)
        
        elif t1[1] == "F":
            valor2 = converte_para_fahrenheit(valor2)
    
    return valor1, valor2
        
def confere_maior_temperatura(t1, t2):
    temp1, temp2 =altera_escala(t1, t2)
    
    if temp1 > temp2:
        resultado = t1
    else:
        resultado = t2
    return resultado

def main():
    print("Digite a primeira temperatura (com valor e escala):")
    t1 = float(input(""))
    escala1 = input("").upper()[0]
    
    print("Digite a segunda temperatura (com valor e escala):")
    t2 = float(input(""))
    escala2 = input("").upper()[0]
    
    temperatura1 = round(t1, 4), escala1
    temperatura2 = round(t2, 4), escala2
    
    print(f"A maior temperatura é: {confere_maior_temperatura(temperatura1, temperatura2)}")
    
if __name__=="__main__":
    main()
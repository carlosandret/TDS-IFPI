# 02. Utilizando a definição de valor da temperatura com tupla da questão anterior, desenvolva uma função que soma
# duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma
# escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve
# ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais.

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
        if t2[1] == "C":
            valor1 = round(converte_para_celsius(valor1), 4)
        
        elif t2[1] == "F":
            valor1 = round(converte_para_fahrenheit(valor1), 4)
    
    return valor1, valor2, t2[1]
        
def soma_temperaturas(t1, t2):
    temp1, temp2, escala =altera_escala(t1, t2)
    
    return round((temp1 + temp2), 4), escala
    
def main():
    t1 = float(input(""))
    escala1 = input("").upper()[0]
    t2 = float(input(""))
    escala2 = input("").upper()[0]
    
    temperatura1 = round(t1, 4), escala1
    temperatura2 = round(t2, 4), escala2
    
    print(f"{soma_temperaturas(temperatura1, temperatura2)}")
if __name__=="__main__":
    main()
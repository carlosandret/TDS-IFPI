# A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair na sua frente. 
# A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que leia quantos 
# metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance a tartaruga. 
# Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.

# Tartaruga --> 1 metro por minuto
# Lebre --> 10 metros por minuto

def main():
    print("-"*70)
    print('''A tartaruga e a lebre vão apostar uma corrida. 
A lebre concede à tartaruga o direito de sair na sua frente. ''')
    print("-"*70)
    print("\nDigite a quantidade de metros que a tartaruga sai a frente da lebre:")
    metros_frente =  int(input("--> "))
    v_tartaruga = 1
    v_lebre = 10
    tempo_vantagem = round(metros_frente / 9)
    print(f"Se a tartaruga sair {metros_frente} metros à frente a lebre à alcança em {tempo_vantagem} minutos.")
    
if __name__=="__main__":
    main()
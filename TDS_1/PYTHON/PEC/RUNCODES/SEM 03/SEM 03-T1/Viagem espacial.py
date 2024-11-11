distancia = float(input('Digite a distância até um planeta em quilômetros? ').strip())
velocidade = float(input('Digite a velocidade da nave em km/h. ').strip())
horas = int((distancia//velocidade))
dias = int((horas//24))
tempo_horas = (horas%24)
print('A viagem levará',dias, "dias e", tempo_horas, "horas")




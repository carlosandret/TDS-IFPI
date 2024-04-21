hora = int(input('Digite o número de horas: ').strip())
minuto = int(input('Digite o número de minutos: ').strip())
segundo = int(input('Digite o número de segundos: ').strip())
tempo_min = hora*60 + minuto 
tempo_seg = (tempo_min * 60) + segundo
print('Passaram',tempo_seg,'segundos desde a última meia-noite.')  
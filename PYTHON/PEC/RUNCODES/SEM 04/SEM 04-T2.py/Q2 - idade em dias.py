anos = int(input('Digite o ano: ').strip())
meses = int(input('Digite o mês: ').strip())
dias = int(input('Digite o dia: ').strip())
resultado = (anos * 365) + (meses * 30) + dias
print(f'A sua idade é de {resultado} dias')
def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

x = int(input('Digite: '))

print(formatar_moeda(x))  # Saída: R$ 49.90
# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.

# Função que confere se um número está presente na lista, retorna um valor booleano
def verifica_num_lista(lista, num):
    if not isinstance(lista, list):
        return Exception
    if not all(isinstance(i, (int, float, str)) for i in lista):
        return Exception
    
    if num in lista:
        return True
    else:
        return False

def main():
    # Testes com a lista de números
    lista_numeros = [1, 5, 9, 7, 3, 10, 54, 20, 6.5, 26]
    
    assert verifica_num_lista(lista_numeros, 9) == True
    assert verifica_num_lista(lista_numeros, 100) == False
    assert verifica_num_lista(lista_numeros, 6.5) == True
    assert verifica_num_lista(lista_numeros, 1) == True
    assert verifica_num_lista(lista_numeros, 7) == True
    assert verifica_num_lista(lista_numeros, 55) == False
    
    # Testes com a lista de strings
    lista_strings = ["maçã", "banana", "laranja", "abacaxi", "melancia"]
    
    assert verifica_num_lista(lista_strings, "banana") == True
    assert verifica_num_lista(lista_strings, "morango") == False
    assert verifica_num_lista(lista_strings, "laranja") == True
    assert verifica_num_lista(lista_strings, "kiwi") == False
    assert verifica_num_lista(lista_strings, "abacaxi") == True
    assert verifica_num_lista(lista_strings, "uva") == False
    
    print("Todos os testes passaram!")
if __name__ == "__main__":
    main()

import pytest 
from veiculos import Veiculo, Carro, Moto

def test_veiculo_basico():
    veiculo = Veiculo("Genérica", "Modelo X", 2000, 20000)
    assert veiculo.ligar() == "O veículo está ligado."
    assert veiculo.desligar() == "O veículo está desligado."
    assert veiculo.calcula_ipva() == None
    assert str(veiculo) == "Marca:Genérica\nModelo: Modelo X\nAno:2000\nValor:20000\n"

def test_carro():
    carro = Carro("VW", "Polo", 2024, 60000, 4)
    assert carro.marca == "VW"
    assert carro.modelo == "Polo"
    assert carro.ano == 2024
    assert carro.valor == 60000
    assert carro.portas == 4
    assert carro.calcula_ipva() == 2400.0  # 4% de 60000
    
    assert str(carro) == "Marca:VW\nModelo: Polo\nAno:2024\nValor:60000\n\n IPVA: 2400.0\n com 4 portas."

def test_carro_isento_ipva():
    fusca = Carro("VW", "Fusca", 1978, 1500, 2)
    assert fusca.calcula_ipva() == 0  # Mais de 10 anos, isento
    assert str(fusca) == "Marca:VW\nModelo: Fusca\nAno:1978\nValor:1500\n\n IPVA: 0\n com 2 portas."

def test_moto():
    moto = Moto("Honda", "Pop", 2015, 10000, 100)
    assert moto.marca == "Honda"
    assert moto.modelo == "Pop"
    assert moto.ano == 2015
    assert moto.valor == 10000
    assert moto.cilindradas == 100
    assert moto.calcula_ipva() == 200.0  # 2% de 10000
    assert str(moto) == "Marca:Honda\nModelo: Pop\nAno:2015\nValor:10000\n\n IPVA: 200.0\n com 100cc."

def test_moto_isenta_ipva():
    moto_antiga = Moto("Yamaha", "RD350", 1980, 5000, 350)
    assert moto_antiga.calcula_ipva() == 0  # Mais de 10 anos, isento
    assert str(moto_antiga) == "Marca:Yamaha\nModelo: RD350\nAno:1980\nValor:5000\n\n IPVA: 0\n com 350cc."

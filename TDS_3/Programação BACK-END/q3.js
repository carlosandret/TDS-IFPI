// 3)​ Implemente uma classe chamada “ContaBancaria” que possua atributos para
// armazenar o número da conta, nome do titular e saldo. Adicione métodos para
// realizar depósitos e saques que recebem como parâmetro o valor.

class ContaBancaria {
    constructor(numeroConta, nomeTitular, saldo) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldo = saldo;
    }
    realizaSaque(valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            return `Saque realizado com sucesso! Seu saldo é de ${this.saldo}.`;
        } else {
            return `Saldo insuficiente! não foi possível realizar o saque.`;
        }
    }
    realizaDeposito(valor) {
        this.saldo += valor;
        return `Depósito feito com sucesso! O seu saldo é de ${this.saldo}`;
    }
}

const conta1 = ContaBancaria(1234, "Joaozin", 0)
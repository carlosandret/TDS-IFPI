import random
class pedra_papel_tesoura:
    escolha_usuario = None
    escolha_computador = None
    vencedor = None

    def obter_escolha_usuario(self):
        escolha = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").strip().lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            self.escolha_usuario = escolha  
            return self.escolha_usuario
        elif escolha == 'sair':
            return None
        else:
            print("Escolha inválida. Tente novamente.")
            return self.obter_escolha_usuario()
        

    def obter_escolha_computador(self):
        self.escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])
        return self.escolha_computador
    
    def determinar_vencedor(self):
        if self.escolha_usuario == self.escolha_computador:
            return "Empate!"
        elif (self.escolha_usuario == 'pedra' and self.escolha_computador == 'tesoura') or \
            (self.escolha_usuario == 'papel' and self.escolha_computador == 'pedra') or \
            (self.escolha_usuario == 'tesoura' and self.escolha_computador == 'papel'):
            return "Você venceu!"
        else:
            return "O computador venceu!"


def main():
    meu_jogo = pedra_papel_tesoura()

    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    while True:
        meu_jogo.escolha_usuario = meu_jogo.obter_escolha_usuario()

        if meu_jogo.escolha_usuario is None:
            print("Encerrando o jogo...")
            break

        meu_jogo.escolha_computador = meu_jogo.obter_escolha_computador()
        print(f"O usuário escolheu: {meu_jogo.escolha_usuario}")
        print(f"Computador escolheu: {meu_jogo.escolha_computador}")

        meu_jogo.vencedor = meu_jogo.determinar_vencedor()
        print(meu_jogo.vencedor)

main()
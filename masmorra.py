from item import Item
from jogador import Jogador
from monstro import Monstro
import random

class Masmorra:
    def __init__(self, nome, jogador, vet_monstros=[]):
        self.nome = nome
        self.jogador = jogador
        self.lista_monstros = vet_monstros

    def adiciona_monstro(self, monstro):
        self.lista_monstros.append(monstro)

    def jogar(self):
        player = self.jogador
        nome_local = self.nome
        vet_monstros = self.lista_monstros
        print(f"Jogador {str(player.nome)} entrou em {str(nome_local)}. \n")

        for monstro in vet_monstros:
            print(f"Monstro {str(monstro.nome)} entrou em {str(nome_local)}. \n")
            while player.pontos_vida>0 and monstro.pontos_vida>0:
                dano = player.atacar()
                monstro.pontos_vida-=dano
                if monstro.pontos_vida > 0:
                    dano = monstro.atacar()
                    player.pontos_vida -= dano
                else:
                    print(f"{monstro.nome} morreu!\n")

            if player.pontos_vida <= 0:
                print(f"{player.nome} morreu!\nO jogo acabou!")
                break


if __name__ == "__main__":
    jog = Jogador("Pope Francis", 250)
    jog.adiciona_item("Espada Sagrada", "Fisico", 5)
    jog.adiciona_item("Bola de fogo", "Mágico", 4)
    jog.adiciona_item("Cruz abençoada", "Mágico", 1)

    mons1 = Monstro("Duende", 50)
    mons1.adiciona_item("Espada curta", "Fisico", 2)
    mons1.adiciona_item("Cutelo", "Fisico", 1)

    mons2 = Monstro("Duende Líder", 80)
    mons2.adiciona_item("Martelo de Guerra", "Fisico", 3)
    mons2.adiciona_item("Espada curta", "Fisico", 2)

    mons3 = Monstro("Aparição", 150)
    mons3.adiciona_item("Corrente de Ar Frio", "Mágico", 5)
    mons3.adiciona_item("Telecinese", "Mágico", 3)

    local = Masmorra("Castelo Assombrado", jog)
    local.adiciona_monstro(mons1)
    local.adiciona_monstro(mons2)
    local.adiciona_monstro(mons3)

    local.jogar()
import random
from item import Item

class Monstro:
    def __init__(self, nome, pontos_vida, vet_itens=[]):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.lista_itens = vet_itens

    def adiciona_item(self, nome, tipo, dano):
        item = Item(nome, tipo, dano)
        self.lista_itens.append(item)

    def atacar(self):
        vet = self.lista_itens

        str_itens = ""
        for itens in self.lista_itens:
            str_itens += f"Itens: {str(itens.nome)}, Tipo do Dano: {str(itens.tipo)}, Poder de dano: {str(itens.dano)}\n"
        print(str_itens)

        escolhido = random.randint(0, len(vet)-1)
        item_esc = vet[escolhido]
        dano = item_esc.atacar()
        str_texto = f"Monstro {self.nome} usou {item_esc.nome} e causou {dano} de dano! \n"

        print(str_texto)
        return dano

    def __str__(self):
        str_itens = ""
        for itens in self.lista_itens:
            str_itens += f"Itens: {str(itens.nome)}, Tipo do Dano: {str(itens.tipo)}, Poder de dano: {str(itens.dano)}\n"

        return "Monstro: " + str(self.nome) + " Pontos de Vida: " + str(self.pontos_vida) + "\n" + str_itens




if __name__ == '__main__':
    mons = Monstro("Dragao Vermelho", 100)
    mons.adiciona_item("Garras", "Fisico", 3)
    mons.adiciona_item("Bola de Fogo", "Mágico", 4)
    mons.adiciona_item("Presas", "Fisico", 3)

    mons1 = Monstro("Humano", 100)
    mons1.adiciona_item("Espada", "Fisico", 3)
    mons1.adiciona_item("Porrete", "Fisico", 3)

    print(mons)
    print(mons1)
    mons.atacar()
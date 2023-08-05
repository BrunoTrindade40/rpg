import random

class Item:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

    def atacar(self):
        return self.dano*random.randint(0, 10)


if __name__ == '__main__':
    item = Item("Espada Justiceira", "Fisico", 2)
    print(f"Nome da arma: {item.nome} \nTipo do dano: {item.tipo} \nDano na rodada: {item.atacar()}")
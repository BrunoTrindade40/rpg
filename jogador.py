import random
from item import Item

class Jogador:
    def __init__(self, nome, pontos_vida, vet_itens=[]):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.lista_itens = vet_itens

    def adiciona_item(self, nome, tipo, dano):
        item = Item(nome, tipo, dano)
        self.lista_itens.append(item)

    def atacar(self):
        vet = self.lista_itens
        escolhido = random.randint(0, len(vet)-1)
        item_esc = vet[escolhido]
        dano = item_esc.atacar()
        str_texto = f"Jogador {self.nome} usou {item_esc.nome} e causou {dano} de dano! \n"

        print(str_texto)
        return dano

    def __str__(self):
        str_itens = ""
        for itens in self.lista_itens:
            str_itens += f"Itens: {str(itens.nome)}, Tipo do Dano: {str(itens.tipo)}, Poder de dano: {str(itens.dano)}\n"

        return "Jogador: " + str(self.nome) + " Pontos de Vida: " + str(self.pontos_vida) + "\n" + str_itens




if __name__ == '__main__':
    jog = Jogador("Sujiro Kimimame", 200)
    jog.adiciona_item("Katana sagrada", "Fisico", 3)
    jog.adiciona_item("Bola de Fogo", "Mágico", 5)
    jog.adiciona_item("Adaga", "Fisico", 1)

    print(jog)
    jog.atacar()
class televisor :

    def __init__(self, fab, modelo):
        self.fabicrante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais =[]
        self.volume = 20


    def aumentsVolume(self,valor):

        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume= 100


    def diminuiVolume(self, valor):

        if self.volume- valor>= 0:
            self.volume-= valor
        else:
            self.volume= 0


    def trocarCanal(self, canal):

        if canal in self.lista_de_canais:
            self.canal_atual= canal

    def sintonizaCanal(self, canal):

        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)


class ControleRemoto:

    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self, tv):
        self.tv = tv

    def diminuiVolume(self):
        self.tv.dimuiVolume(90)

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizacanal(canal)
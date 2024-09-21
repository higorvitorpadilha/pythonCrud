class conta:
    def __init__(self,titular,numero,saldo):
        self.saldo=0
        self.numero=numero
        self.titular=titular

        @property
        def getsaldo(self) :
            return self._saldo
        @saldo.setter
        def setsaldo(self, saldo):
            if (saldo<0):
                print("O saldo não pode ser negativo")
            else:
                self.saldo = saldo

        def saque(self,valor):
            if(self.saldo>=valor):
                print("Saque realizado com sucesso ")
            else:
                print("Saldo insuficiente")
        def deposita(self, valor):
            self.saldo+=valor
        def extrato(self):
            print("Cliente: ", self.titular,"Saldo atual: ", self._saldo)
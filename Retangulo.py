class Retangulo:
    def __init__(self,lado_a,lado_b):
        self.a= lado_a
        self.b = lado_b

    def Muda_Valor(self,novo_a, novo_b):
        self.a = novo_a
        self.b= novo_b

    def Retorna_Lado(self):
        print(f'O retângulo possui dimensôes {self.a} m x {self.b}m')

    def area(self):
        return self.a * self.b
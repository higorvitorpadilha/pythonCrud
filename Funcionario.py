class Funcionario:
    def __init__(self,nome,email):
        self.nome= nome
        self.email = email
        self.horas = {}
        self.salario_hora= {}

    def Cadastro_Hora(self,mes, horas):
        if(mes not in self.horas):
            self.horas[mes] = horas

    def Cadastro_Salario_Hora (self,mes,valor):
        if(mes not in self.salario_hora):
            self.salario_hora[mes]= valor


    def Calcula_Salario (self,mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print('Mes inexistente')
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):
        return f'Funcionario: {self.nome} \nEmail: {self.email} \nhoras mes: {self.horas} \nSalario-hora {self.salario_hora}'

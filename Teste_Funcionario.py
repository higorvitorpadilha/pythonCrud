from  Funcionario import Funcionario

funcionario= Funcionario ('Matheus', 'Matehus@blablabla.com.br')

funcionario.Cadastro_Hora('jan', 300)
funcionario.Cadastro_Hora('fev', 200)
funcionario.Cadastro_Salario_Hora('jan', 30)
funcionario.Cadastro_Salario_Hora('fev', 30)
print(funcionario)
print(funcionario.Calcula_Salario('jan'))
print(funcionario.Calcula_Salario('fev'))


class main:
    nome="Ana"
    print(len(nome))


from Cliente import  Cliente

from Conta import conta

#c1= Cliente("JOÃO","11444-2222")
#conta=conta(c1._nome,6568,0)

conta.deposita(1000)
conta.saque(50)
conta.extrato()

#print(c1)
#print(c1._nome," e " ,c1._telefone)

#print(conta.titular, 'Numero: ', conta.numero, "Seu saldo: ", conta._saldo)
from tkinter import  *
import tkinter as tk
class Gui () :
    """Classe da interface gráfica"""

    x_pad=5
    y_pad=3
    width_entry=30








# Criando labels
window = tk.Tk()
window.title("Gerenciador de Clientes")

# Definindo a largura dos campos de entrada
width_entry = 30

# Criando as variáveis de controle para os campos de entrada
txtNome = tk.StringVar()
txtSobrenome = tk.StringVar()
txtEmail = tk.StringVar()
txtCPF = tk.StringVar()

# Criando os objetos da interface gráfica
lblNome = tk.Label(window, text="Nome:")
lblSobrenome = tk.Label(window, text="Sobrenome:")
lblEmail = tk.Label(window, text="Email:")
lblCPF = tk.Label(window, text="CPF:")
entNome = tk.Entry(window, textvariable=txtNome, width=width_entry)
entSobrenome = tk.Entry(window, textvariable=txtSobrenome, width=width_entry)
entEmail = tk.Entry(window, textvariable=txtEmail, width=width_entry)
entCPF = tk.Entry(window, textvariable=txtCPF, width=width_entry)
listClientes = tk.Listbox(window, width=100)
scrollClientes = tk.Scrollbar(window)
btnViewAll = tk.Button(window, text="Ver todos")
btnBuscar = tk.Button(window, text="Buscar")
btnInserir = tk.Button(window, text="Inserir")
btnUpdate = tk.Button(window, text="Atualizar Selecionados")
btnDel = tk.Button(window, text="Deletar Selecionados")
btnClose = tk.Button(window, text="Fechar")

btnViewAll = tk.Button(root, text="Visualizar Todos")
btnBuscar = tk.Button(root, text="Buscar")
btnInserir = tk.Button(root, text="Inserir")
btnUpdate = tk.Button(root, text="Atualizar")
btnDel = tk.Button(root, text="Deletar")
btnClose = tk.Button(root, text="Fechar")

# Posicione os widgets usando grid
lblnome.grid(row=0, column=0)
lblsobrenome.grid(row=1, column=0)
lblemail.grid(row=2, column=0)
lblcpf.grid(row=3, column=0)

entNome.grid(row=0, column=1, padx=50, pady=50)
entSobrenome.grid(row=1, column=1)
entEmail.grid(row=2, column=1)
entCPF.grid(row=3, column=1)

listClientes.grid(row=0, column=2, rowspan=10)
scrollClientes.grid(row=0, column=6, rowspan=10)

btnViewAll.grid(row=4, column=0, columnspan=2)
btnBuscar.grid(row=5, column=0, columnspan=2)
btnInserir.grid(row=6, column=0, columnspan=2)
btnUpdate.grid(row=7, column=0, columnspan=2)
btnDel.grid(row=8, column=0, columnspan=2)
btnClose.grid(row=9, column=0, columnspan=2)

listClientes.configure(yscrollcommand=scrollClientes.set)
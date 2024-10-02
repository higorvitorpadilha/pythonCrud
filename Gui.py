import tkinter as tk

class Gui:
    """Classe da interface gráfica"""

    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        # Criando a janela principal
        self.window = tk.Tk()
        self.window.title("Gerenciador de Clientes")

        # Criando as variáveis de controle para os campos de entrada
        self.txtNome = tk.StringVar()
        self.txtSobrenome = tk.StringVar()
        self.txtEmail = tk.StringVar()
        self.txtCPF = tk.StringVar()

        # Criando os objetos da interface gráfica
        lblNome = tk.Label(self.window, text="Nome:")
        lblSobrenome = tk.Label(self.window, text="Sobrenome:")
        lblEmail = tk.Label(self.window, text="Email:")
        lblCPF = tk.Label(self.window, text="CPF:")
        self.entNome = tk.Entry(self.window, textvariable=self.txtNome, width=Gui.width_entry)
        self.entSobrenome = tk.Entry(self.window, textvariable=self.txtSobrenome, width=Gui.width_entry)
        self.entEmail = tk.Entry(self.window, textvariable=self.txtEmail, width=Gui.width_entry)
        self.entCPF = tk.Entry(self.window, textvariable=self.txtCPF, width=Gui.width_entry)
        self.listClientes = tk.Listbox(self.window, width=100)
        scrollClientes = tk.Scrollbar(self.window)

        # Botões
        self.btnViewAll = tk.Button(self.window, text="Ver todos")
        self.btnBuscar = tk.Button(self.window, text="Buscar")
        self.btnInserir = tk.Button(self.window, text="Inserir")
        self.btnUpdate = tk.Button(self.window, text="Atualizar Selecionados")
        self.btnDel = tk.Button(self.window, text="Deletar Selecionados")
        btnClose = tk.Button(self.window, text="Fechar", command=self.window.destroy)

        # Posicione os widgets usando grid
        lblNome.grid(row=0, column=0)
        lblSobrenome.grid(row=1, column=0)
        lblEmail.grid(row=2, column=0)
        lblCPF.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=Gui.x_pad, pady=Gui.y_pad)
        self.entSobrenome.grid(row=1, column=1, padx=Gui.x_pad, pady=Gui.y_pad)
        self.entEmail.grid(row=2, column=1, padx=Gui.x_pad, pady=Gui.y_pad)
        self.entCPF.grid(row=3, column=1, padx=Gui.x_pad, pady=Gui.y_pad)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        scrollClientes.grid(row=0, column=3, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2, pady=Gui.y_pad)
        self.btnBuscar.grid(row=5, column=0, columnspan=2, pady=Gui.y_pad)
        self.btnInserir.grid(row=6, column=0, columnspan=2, pady=Gui.y_pad)
        self.btnUpdate.grid(row=7, column=0, columnspan=2, pady=Gui.y_pad)
        self.btnDel.grid(row=8, column=0, columnspan=2, pady=Gui.y_pad)
        btnClose.grid(row=9, column=0, columnspan=2, pady=Gui.y_pad)

        self.listClientes.configure(yscrollcommand=scrollClientes.set)
        scrollClientes.configure(command=self.listClientes.yview)

    def run(self):
        self.window.mainloop()

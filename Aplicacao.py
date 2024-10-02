from Gui import *
import Backend as core
import tkinter as tk

app = None
selected = None  # Ensure selected is declared globally

def view_command():
    rows = core.TransactionObject.view()
    app.listClientes.delete(0, tk.END)
    for r in rows:
        app.listClientes.insert(tk.END, r)

def search_command():
    app.listClientes.delete(0, tk.END)
    rows = core.TransactionObject.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(tk.END, r)

def insert_command():
    core.TransactionObject.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    if selected:
        core.TransactionObject.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
        view_command()

def del_command():
    if selected:
        id = selected[0]
        core.TransactionObject.delete(id)
        view_command()

def getSelectedRow(event):
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)

        # Populate the entry fields with the selected row's data
        app.entNome.delete(0, tk.END)
        app.entNome.insert(tk.END, selected[1])
        app.entSobrenome.delete(0, tk.END)
        app.entSobrenome.insert(tk.END, selected[2])
        app.entEmail.delete(0, tk.END)
        app.entEmail.insert(tk.END, selected[3])
        app.entCPF.delete(0, tk.END)
        app.entCPF.insert(tk.END, selected[4])
    except IndexError:
        selected = None  # Handle case where no item is selected

if __name__ == "__main__":
    app = Gui()

    # Bind the listbox selection event to getSelectedRow
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    # Configure button commands
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)

    # Start the application
    app.run()

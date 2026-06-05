from tkinter import *
class clientes:
    def __init__(self, ventanaPrincipal):
        self.ventanaClientes = Toplevel(ventanaPrincipal)
        self.ventanaClientes.title("Administación de los datos de los clientes")
        self.ventanaClientes.geometry("700x500")

        self.ventanaClientes.focus_set()
        self.ventanaClientes.grab_set()
        self.ventanaClientes.transient(master=ventanaPrincipal)
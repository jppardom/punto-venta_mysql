from tkinter import *
from clientes import clientes 

class principal:
    def __init__(self, nombre):
        self.ventanaPrinipal = Tk()
        self.ventanaPrinipal.title("Ventana principal del sistema                                   Hola "+nombre)

        self.ventanaPrinipal.geometry("1000x700")

        #BarraMenu
        self.barraMenu = Menu(self.ventanaPrinipal)
        self.ventanaPrinipal.config(menu=self.barraMenu)
        

        #Crear Menús
        self.archivoMenu = Menu(self.barraMenu, tearoff=0)
        self.archivoMenu = Menu(self.barraMenu, tearoff=0)

        self.AdministracionMenu = Menu(self.barraMenu, tearoff=0)
        self.mantenimientoMenu = Menu (self.barraMenu, tearoff=0)
        self.ayudaMenu = Menu (self.barraMenu, tearoff=0)
       

        #SubMenus
        self.archivoMenu.add_command(label="Acerca de")
        self.archivoMenu.add_command(label="Salir")

        self.AdministracionMenu.add_command(label="Clientes", command=lambda:clientes.__init__(self, self.ventanaPrinipal))
        self.AdministracionMenu.add_command(label="Productos")
        self.AdministracionMenu.add_command(label="Proveedores")

        self.mantenimientoMenu.add_command(label="Facturación")

        self.ayudaMenu.add_command(label="Ayuda")

        self.barraMenu.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.barraMenu.add_cascade(label="Administración", menu=self.AdministracionMenu)
        self.barraMenu.add_cascade(label="Mantenimiento", menu=self.mantenimientoMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)


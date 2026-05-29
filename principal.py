from tkinter import *

class principal:
    def __init__(self, nombre):
        self.ventanaPrinipal = Tk()
        self.ventanaPrinipal.title("Ventana principal del sistema                                   Hola "+nombre)
        self.ventanaPrinipal.geometry("800x600")
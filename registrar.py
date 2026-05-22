from tkinter import *
from conexion import conexion
from hashlib import sha1

class registrar:
    def __init__(self):
        self.ventanaRegistar = Tk()
        self.ventanaRegistar.title("Ventana para registrar usuarios")
        self.frame = LabelFrame (self.ventanaRegistar, text="Registro de Usuarios")
        self.frame.config(font=("Comic Sans MS", 18))
        self.frame.pack()

        self.lbl = Label (self.frame, text="Cédula ")
        self.lbl.grid(column=2, row=1, padx=7, pady=7, columnspan=2)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtCedula = Entry(self.frame)
        self.txtCedula.grid(column=3, row=1, padx=7, pady=7, columnspan=2, sticky=W)
        self.txtCedula.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Nombres")
        self.lbl.grid(column=1, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtNombres = Entry(self.frame)
        self.txtNombres.grid(column=2, row=2, padx=7, pady=7)
        self.txtNombres.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Apellidos")
        self.lbl.grid(column=3, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtApellidos = Entry(self.frame)
        self.txtApellidos.grid(column=4, row=2, padx=7, pady=7)
        self.txtApellidos.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Correo")
        self.lbl.grid(column=1, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtCorreo = Entry(self.frame)
        self.txtCorreo.grid(column=2, row=3, padx=7, pady=7)
        self.txtCorreo.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Direccion")
        self.lbl.grid(column=3, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtDireccion = Entry(self.frame)
        self.txtDireccion.grid(column=4, row=3, padx=7, pady=7)
        self.txtDireccion.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Usuario")
        self.lbl.grid(column=1, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtUsuario = Entry(self.frame)
        self.txtUsuario.grid(column=2, row=4, padx=7, pady=7)
        self.txtUsuario.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Contraseña")
        self.lbl.grid(column=3, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtPassword = Entry(self.frame)
        self.txtPassword.grid(column=4, row=4, padx=7, pady=7)
        self.txtPassword.config(font=("Comic Sans MS", 14), show="*")

        self.btnGuardar = Button(self.frame, text="GUARDAR", width=10, command=lambda:registrar.guardar(self))
        self.btnGuardar.grid(column=2, row=5, padx=7, pady=7, columnspan=2)
        self.btnGuardar.config(font=("Comic Sans MS", 14))

        self.btnCancelar = Button(self.frame, text="CANCELAR", width=10)
        self.btnCancelar.grid(column=3, row=5, padx=7, pady=7, columnspan=2, sticky=W)
        self.btnCancelar.config(font=("Comic Sans MS", 14))

    def guardar (self):
        
        password = sha1(self.txtPassword.get().encode('utf-8')).hexdigest()
        print (self.txtPassword.get())
        print(password) 
        sql = "INSERT INTO usuario (cedula, nombres, apellidos, direccion, correo, usuario, password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
from tkinter import *
from tkinter import messagebox
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
        if self.txtCedula.get() != "" and self.txtNombres.get() != "" and self.txtApellidos.get() != "" and self.txtDireccion.get() != "" and self.txtCorreo.get() != "" and self.txtUsuario.get() != "" and self.txtPassword.get() != "":
            password = sha1(self.txtPassword.get().encode('utf-8')).hexdigest()
            sql = "INSERT INTO usuario (cedula, nombres, apellidos, direccion, correo, usuario, password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            parametros = (self.txtCedula.get(), self.txtNombres.get(), self.txtApellidos.get(), self.txtDireccion.get(), self.txtCorreo.get(), self.txtUsuario.get(), password)
            if conexion.ejecutarSQL(sql, parametros):
                messagebox.showinfo(title="Guardar datos", message="Datos de usuario guardados correctamente...!")
                registrar.limpiar(self)
            else:
                messagebox.showerror(title="Error", message="Los datos de usuario no puede ser guardados..!")
            
        else:
            messagebox.showwarning(title="Datos del formulario", message="Este formulario posee compos obligatorios")
    
    def limpiar (self):
        self.txtCedula.delete(0,'end')
        self.txtNombres.delete(0,'end')
        self.txtApellidos.delete(0,'end')
        self.txtDireccion.delete(0,'end')
        self.txtCorreo.delete(0,'end')
        self.txtUsuario.delete(0,'end')
        self.txtPassword.delete(0,'end')

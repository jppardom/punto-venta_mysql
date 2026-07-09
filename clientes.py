from tkinter import *
from tkinter import ttk
from conexion import conexion
from tkinter import messagebox
class clientes:
    def __init__(self, ventanaPrincipal):
        self.ventanaClientes = Toplevel(ventanaPrincipal)
        self.ventanaClientes.title("Administación de los datos de los clientes")
        self.ventanaClientes.geometry("1000x700")
        

        self.ventanaClientes.focus_set()
        self.ventanaClientes.grab_set()
        self.ventanaClientes.transient(master=ventanaPrincipal)

        self.frame = LabelFrame(self.ventanaClientes, text='Datos del cliente')
        self.frame.config(font=("Comic Sans MS", 16))
        self.frame.grid(column=1, row=1, padx=7, pady=7, columnspan=4)

        self.lbl = Label (self.frame, text="Cédula ")
        self.lbl.grid(column=2, row=1, padx=7, pady=7, columnspan=2)
        self.lbl.config(font=("Comic Sans MS", 12))
        
        self.txtCedula = Entry (self.frame)
        self.txtCedula.grid(column=3, row=1, padx=7, pady=7, columnspan=2)
        self.txtCedula.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Nombres")
        self.lbl.grid(column=1, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtNombres = Entry(self.frame)
        self.txtNombres.grid(column=2, row=2, padx=7, pady=7)
        self.txtNombres.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Apellidos")
        self.lbl.grid(column=3, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtApellidos = Entry(self.frame)
        self.txtApellidos.grid(column=4, row=2, padx=7, pady=7)
        self.txtApellidos.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Género")
        self.lbl.grid(column=1, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.cbxGenero = ttk.Combobox(self.frame)
        self.cbxGenero['values'] = ("[Seleccione]", "Masculino", "Femenino")
        self.cbxGenero.current(0)
        self.cbxGenero.grid(column=2, row=3, padx=7, pady=7)
        self.cbxGenero.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Teléfono")
        self.lbl.grid(column=3, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtTelefono = Entry(self.frame)
        self.txtTelefono.grid(column=4, row=3, padx=7, pady=7)
        self.txtTelefono.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Correo")
        self.lbl.grid(column=1, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtCorreo = Entry(self.frame)
        self.txtCorreo.grid(column=2, row=4, padx=7, pady=7)
        self.txtCorreo.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Direccion")
        self.lbl.grid(column=3, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtDireccion = Entry(self.frame)
        self.txtDireccion.grid(column=4, row=4, padx=7, pady=7)
        self.txtDireccion.config(font=("Comic Sans MS", 12))

        self.frameBotones = LabelFrame(self.ventanaClientes, text="Funcionalidad")
        self.frameBotones.config(font=("Comic Sans MS", 16))
        self.frameBotones.grid(column=5, row=1, padx=7, pady=7)

        self.btnNuevo = Button(self.frameBotones, text="Nuevo", width=10, command=lambda:clientes.desbloquearGuardar(self))
        self.btnNuevo.config(font=("Comic Sans MS", 12))
        self.btnNuevo.grid(column=6, row=1, padx=7, pady=7)

        self.btnGuardar = Button(self.frameBotones, text="Guardar", width=10, command=lambda:clientes.guardarDatos(self))
        self.btnGuardar.config(font=("Comic Sans MS", 12))
        self.btnGuardar.grid(column=6, row=2, padx=7, pady=7)

        self.btnActualizar = Button(self.frameBotones, text="Actualizar", width=10)
        self.btnActualizar.config(font=("Comic Sans MS", 12))
        self.btnActualizar.grid(column=6, row=3, padx=7, pady=7)

        self.btnCancelar = Button(self.frameBotones, text="Cancelar", width=10, command=lambda:clientes.bloquear(self))
        self.btnCancelar.config(font=("Comic Sans MS", 12))
        self.btnCancelar.grid(column=6, row=4, padx=7, pady=7)

        self.frameTabla = LabelFrame (self.ventanaClientes, text="Datos del cliente")
        self.frameTabla.config(font=("Comic Sans MS", 16))
        self.frameTabla.grid(column=1, row=5, padx=7, pady=7, columnspan=8)

   
        self.tabla = ttk.Treeview(self.frameTabla, height=10, columns= ("id","cedula", "apellidos", "nombres", "genero",
                                                                         "telefono", "correo", "direccion"), show="headings")
        self.tabla.grid(column=1, row=6, padx=7, pady=7, columnspan=8)
        self.tabla.heading("id", text="ID", anchor="center")
        self.tabla.column("id", width=50)
        self.tabla.heading("cedula", text="CÉDULA", anchor="center")
        self.tabla.column("cedula", width=100)
        self.tabla.heading("apellidos", text="APELLIDOS", anchor="center")
        self.tabla.column("apellidos", width=100)
        self.tabla.heading("nombres", text="NOMBRES ", anchor="center")
        self.tabla.column("nombres", width=100)
        self.tabla.heading("genero", text="GÉNERO", anchor="center")
        self.tabla.column("genero", width=100)
        self.tabla.heading("telefono", text="TELÉFONO", anchor="center")
        self.tabla.column("telefono", width=100)
        self.tabla.heading("correo", text="CORREO", anchor="center")
        self.tabla.column("correo", width=200)
        self.tabla.heading("direccion", text="DIRECCIÓN", anchor="center")
        self.tabla.column("direccion", width=200)

        clientes.bloquear(self)

    def bloquear (self):
        self.txtCedula.config(state="disabled")
        self.txtApellidos.config(state="disabled")
        self.txtNombres.config(state="disabled")
        self.cbxGenero["state"] = "disabled"
        self.txtTelefono.config(state="disabled")
        self.txtCorreo.config(state="disabled")
        self.txtDireccion.config(state="disabled")
        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(state="disabled")
        self.btnActualizar.config(state="disabled")
        self.btnCancelar.config(state="disabled")

    def desbloquearGuardar (self):
        self.txtCedula.config(state="normal")
        self.txtApellidos.config(state="normal")
        self.txtNombres.config(state="normal")
        self.cbxGenero["state"] = "normal"
        self.txtTelefono.config(state="normal")
        self.txtCorreo.config(state="normal")
        self.txtDireccion.config(state="normal")
        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnActualizar.config(state="disabled")
        self.btnCancelar.config(state="normal")
        self.txtCedula.focus()
    
    def guardarDatos (self):
        sql = """INSERT INTO clientes (cedula, nombres, apellidos, genero, telefono, correo, direccion)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        parametros = (self.txtCedula.get(), self.txtNombres.get(), self.txtApellidos.get(), self.cbxGenero.get(),
                      self.txtTelefono.get(), self.txtCorreo.get(), self.txtDireccion.get())
        if (conexion.ejecutarSQL(sql, parametros)):
            messagebox.showinfo(title="Guardar datos de los clientes", message="Datos del cliente almancedos correctamen ...")
            clientes.limpiar(self)
            clientes.bloquear(self)
        else:
            messagebox.showerror(title="Guardar datos de los clientes", message="Los datos del cliente no pueden ser guardados ...")
    
    def limpiar (self):
        self.txtCedula.delete(0, "end")
        self.txtApellidos.delete(0, "end")
        self.txtNombres.delete(0, "end")
        self.cbxGenero.delete(0, "end")
        self.txtTelefono.delete(0, "end")
        self.txtCorreo.delete(0, "end")
        self.txtDireccion.delete(0, "end")
        self.txtCedula.focus()
    # def cargarTabla(self):
    #     self.limpiar_tabla = self.tabla.get_children()
    #     for elemento in self.limpiar_tabla:
    #         self.tabla.delete(elemento)
    #     self.sql = "" 


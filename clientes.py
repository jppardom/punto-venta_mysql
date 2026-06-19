from tkinter import *
from tkinter import ttk
class clientes:
    def __init__(self, ventanaPrincipal):
        self.ventanaClientes = Toplevel(ventanaPrincipal)
        self.ventanaClientes.title("Administación de los datos de los clientes")
        self.ventanaClientes.geometry("1000x700")

        self.ventanaClientes.focus_set()
        self.ventanaClientes.grab_set()
        self.ventanaClientes.transient(master=ventanaPrincipal)

        self.frame = LabelFrame(self.ventanaClientes, text='Datos del cliente')
        self.frame.config(font=("Comic Sans MS", 18))
        self.frame.grid(column=1, row=1, padx=7, pady=7, columnspan=4)

        self.lbl = Label (self.frame, text="Cédula ")
        self.lbl.grid(column=2, row=1, padx=7, pady=7, columnspan=2)
        self.lbl.config(font=("Comic Sans MS", 14))
        
        self.txtCedula = Entry (self.frame)
        self.txtCedula.grid(column=3, row=1, padx=7, pady=7, columnspan=2)
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

        self.lbl = Label (self.frame, text="Género")
        self.lbl.grid(column=1, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.cbxGenero = ttk.Combobox(self.frame)
        self.cbxGenero['values'] = ("[Seleccione]", "Femenino", "Feminino")
        self.cbxGenero.current(0)
        self.cbxGenero.grid(column=2, row=3, padx=7, pady=7)
        self.cbxGenero.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Género")
        self.lbl.grid(column=3, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtTelefono = Entry(self.frame)
        self.txtTelefono.grid(column=4, row=3, padx=7, pady=7)
        self.txtTelefono.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Correo")
        self.lbl.grid(column=1, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtCorreo = Entry(self.frame)
        self.txtCorreo.grid(column=2, row=4, padx=7, pady=7)
        self.txtCorreo.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Direccion")
        self.lbl.grid(column=3, row=4, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtDireccion = Entry(self.frame)
        self.txtDireccion.grid(column=4, row=4, padx=7, pady=7)
        self.txtDireccion.config(font=("Comic Sans MS", 14))

        self.frameBotones = LabelFrame(self.ventanaClientes, text="Funcionalidad")
        self.frameBotones.config(font=("Comic Sans MS", 18))
        self.frameBotones.grid(column=5, row=1, padx=7, pady=7)

        self.btnNuevo = Button(self.frameBotones, text="Nuevo", width=10)
        self.btnNuevo.config(font=("Comic Sans MS", 14))
        self.btnNuevo.grid(column=6, row=1, padx=7, pady=7)

        self.btnGuardar = Button(self.frameBotones, text="Guardar", width=10)
        self.btnGuardar.config(font=("Comic Sans MS", 14))
        self.btnGuardar.grid(column=6, row=2, padx=7, pady=7)

        self.btnActualizar = Button(self.frameBotones, text="Actualizar", width=10)
        self.btnActualizar.config(font=("Comic Sans MS", 14))
        self.btnActualizar.grid(column=6, row=3, padx=7, pady=7)

        self.btnCancelar = Button(self.frameBotones, text="Cancelar", width=10)
        self.btnCancelar.config(font=("Comic Sans MS", 14))
        self.btnCancelar.grid(column=6, row=4, padx=7, pady=7)

        self.frameTabla = LabelFrame (self.ventanaClientes, text="Datos del cliente")
        self.frameTabla.config(font=("Comic Sans MS", 18))
        self.frameTabla.grid(column=1, row=5, padx=7, pady=7)

   
        self.tabla = ttk.Treeview(self.frameTabla, height=10, columns= ("id","cedula", "apellidos", "nombres", "genero",
                                                                         "telefono", "correo", "direccion"), show="headings")
        self.tabla.grid(column=1, row=6, padx=7, pady=7, columnspan=8)



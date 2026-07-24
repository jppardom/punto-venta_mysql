from tkinter import *
from tkinter import ttk
from conexion import conexion
from tkinter import messagebox
class productos:
    def __init__(self, ventanaPrincipal):
        self.ventanaProductos = Toplevel(ventanaPrincipal)
        self.ventanaProductos.title("Administación de los datos de prouctos")
        self.ventanaProductos.geometry("1000x700")
        

        self.ventanaProductos.focus_set()
        self.ventanaProductos.grab_set()
        self.ventanaProductos.transient(master=ventanaPrincipal)

        self.frame = LabelFrame(self.ventanaProductos, text='Datos de productos')
        self.frame.config(font=("Comic Sans MS", 16))
        self.frame.grid(column=1, row=1, padx=7, pady=7, columnspan=4)

        self.lbl = Label (self.frame, text="Nombre")
        self.lbl.grid(column=1, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtNombre = Entry(self.frame)
        self.txtNombre.grid(column=2, row=2, padx=7, pady=7)
        self.txtNombre.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Stock")
        self.lbl.grid(column=3, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtStock = Entry(self.frame)
        self.txtStock.grid(column=4, row=2, padx=7, pady=7)
        self.txtStock.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Precio")
        self.lbl.grid(column=1, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtPrecio = Entry(self.frame)  
        self.txtPrecio.grid(column=2, row=3, padx=7, pady=7)
        self.txtPrecio.config(font=("Comic Sans MS", 12))

        self.lbl = Label (self.frame, text="Descrpción")
        self.lbl.grid(column=3, row=3, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 12))

        self.txtDescripcion = Entry(self.frame)
        self.txtDescripcion.grid(column=4, row=3, padx=7, pady=7)
        self.txtDescripcion.config(font=("Comic Sans MS", 12))

        self.frameBotones = LabelFrame(self.ventanaProductos, text="Funcionalidad")
        self.frameBotones.config(font=("Comic Sans MS", 16))
        self.frameBotones.grid(column=5, row=1, padx=7, pady=7)

        self.btnNuevo = Button(self.frameBotones, text="Nuevo", width=10, command=lambda:productos.desbloquearGuardar(self))
        self.btnNuevo.config(font=("Comic Sans MS", 12))
        self.btnNuevo.grid(column=6, row=1, padx=7, pady=7)

        self.btnGuardar = Button(self.frameBotones, text="Guardar", width=10, command=lambda:productos.guardarDatos(self))
        self.btnGuardar.config(font=("Comic Sans MS", 12))
        self.btnGuardar.grid(column=6, row=2, padx=7, pady=7)

        self.btnActualizar = Button(self.frameBotones, text="Actualizar", width=10, command=lambda:productos.actualizar(self))
        self.btnActualizar.config(font=("Comic Sans MS", 12))
        self.btnActualizar.grid(column=6, row=3, padx=7, pady=7)

        self.btnCancelar = Button(self.frameBotones, text="Cancelar", width=10, command=lambda:productos.bloquear(self))
        self.btnCancelar.config(font=("Comic Sans MS", 12))
        self.btnCancelar.grid(column=6, row=4, padx=7, pady=7)

        self.frameTabla = LabelFrame (self.ventanaProductos, text="Datos de productos")
        self.frameTabla.config(font=("Comic Sans MS", 16))
        self.frameTabla.grid(column=1, row=5, padx=7, pady=7, columnspan=8)

        self.popup = Menu (self.frameTabla, tearoff= 0)
        self.popup.add_command(label="EDITAR", command=lambda:productos.editar(self))
        self.popup.add_command(label="ELIMINAR", command=lambda:productos.eliminar(self))
        def do_popup(event):
            # display the popup menu
            try:
                self.popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.popup.grab_release()
   
        self.tabla = ttk.Treeview(self.frameTabla, height=10, columns= ("id","nombre", "stock", "precio", "descripcion",), show="headings")
        self.tabla.grid(column=1, row=6, padx=7, pady=7, columnspan=5)
        self.tabla.heading("id", text="ID", anchor="center")
        self.tabla.column("id", width=50)
        self.tabla.heading("nombre", text="NOMBRE", anchor="center")
        self.tabla.column("nombre", width=200)
        self.tabla.heading("stock", text="STOCK", anchor="center")
        self.tabla.column("stock", width=100)
        self.tabla.heading("precio", text="PRECIO ", anchor="center")
        self.tabla.column("precio", width=100)
        self.tabla.heading("descripcion", text="DESCRIPCIÓN", anchor="center")
        self.tabla.column("descripcion", width=400)
        
        self.tabla.bind("<Button-3>", do_popup)
        self.cod_cliente = 0

        productos.cargarTabla(self)
        productos.bloquear(self)
        

    def bloquear (self):
        productos.limpiar(self)
        self.txtNombre.config(state="disabled")
        self.txtStock.config(state="disabled")
        self.txtPrecio.config(state="disabled")
        self.txtDescripcion.config(state="disabled")
        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(state="disabled")
        self.btnActualizar.config(state="disabled")
        self.btnCancelar.config(state="disabled")

    def desbloquearGuardar (self):
        self.txtNombre.config(state="normal")
        self.txtStock.config(state="normal")
        self.txtPrecio.config(state="normal")
        self.txtDescripcion.config(state="normal")
        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnActualizar.config(state="disabled")
        self.btnCancelar.config(state="normal")
        self.txtNombre.focus()
    
    def guardarDatos (self):
        sql = """INSERT INTO clientes (cedula, nombres, apellidos, genero, telefono, correo, direccion)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        parametros = (self.txtCedula.get(), self.txtNombres.get(), self.txtApellidos.get(), self.cbxGenero.get(),
                      self.txtTelefono.get(), self.txtCorreo.get(), self.txtDireccion.get())
        if (conexion.ejecutarSQL(sql, parametros)):
            messagebox.showinfo(title="Guardar datos de los clientes", message="Datos del cliente almancedos correctamen ...")
            clientes.limpiar(self)
            clientes.bloquear(self)
            clientes.cargarTabla(self)
        else:
            messagebox.showerror(title="Guardar datos de los clientes", message="Los datos del cliente no pueden ser guardados ...")
    
    def limpiar (self):
        self.txtNombre.delete(0, "end")
        self.txtStock.delete(0, "end")
        self.txtPrecio.delete(0, "end")
        self.txtDescripcion.delete(0, "end")
        
        self.txtNombre.focus()

    def cargarTabla(self):
        self.limpiar_tabla = self.tabla.get_children()
        for elemento in self.limpiar_tabla:
            self.tabla.delete(elemento)
        sql = "SELECT * FROM productos"
        data = conexion.ejecutarSQL(sql)
        for fila in data:
            self.tabla.insert("", fila[0],values=(fila[0], fila[1], fila[3], fila[2], fila[4]))

    def debloquearActualizar (self):
        self.txtCedula.config(state="normal")
        self.txtApellidos.config(state="normal")
        self.txtNombres.config(state="normal")
        self.cbxGenero["state"] = "normal"
        self.txtTelefono.config(state="normal")
        self.txtCorreo.config(state="normal")
        self.txtDireccion.config(state="normal")
        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="disabled")
        self.btnActualizar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.txtCedula.focus()

    def editar(self):
        try:
            self.cod_cliente = self.tabla.item(self.tabla.selection())['values'][0]
        except IndexError as e:
            messagebox.showwarning(title="Selección de la fila", message="Primero seleccione una fila de la tabla")
            return
        clientes.debloquearActualizar (self)
        self.cod_cliente = self.tabla.item(self.tabla.selection())['values'][0]
        self.txtCedula.insert(0, self.tabla.item(self.tabla.selection())['values'][1])
        self.txtCedula.config(state="disabled")
        self.txtNombres.insert(0, self.tabla.item(self.tabla.selection())['values'][3])
        self.txtApellidos.insert(0, self.tabla.item(self.tabla.selection())['values'][2])
        self.cbxGenero.insert(0, self.tabla.item(self.tabla.selection())['values'][4])
        self.txtTelefono.insert(0, self.tabla.item(self.tabla.selection())['values'][5])
        self.txtCorreo.insert(0, self.tabla.item(self.tabla.selection())['values'][6])
        self.txtDireccion.insert(0, self.tabla.item(self.tabla.selection())['values'][7])

    def actualizar (self):
        sql = """UPDATE clientes SET nombres=%s, apellidos=%s, genero=%s, telefono=%s, correo=%s, direccion=%s
                WHERE id_cliente=%s"""
        parametros = (self.txtNombres.get(), self.txtApellidos.get(), self.cbxGenero.get(),
                      self.txtTelefono.get(), self.txtCorreo.get(), self.txtDireccion.get(), self.cod_cliente)
        if (conexion.ejecutarSQL(sql, parametros)):
            messagebox.showinfo(title="Actualizar datos de los clientes", message="Datos del cliente actualizados correctamente ...")
            self.txtCedula.config(state="normal")
            clientes.limpiar(self)
            clientes.bloquear(self)
            clientes.cargarTabla(self)
        else:
            messagebox.showerror(title="Actualizar datos de los clientes", message="Los datos del cliente no pueden ser actualizados ...")

    def eliminar(self):
        try:
            self.cod_cliente = self.tabla.item(self.tabla.selection())['values'][0]
        except IndexError as e:
            messagebox.showwarning(title="Selección de la fila", message="Primero seleccione una fila de la tabla")
            return
        sql = "DELETE FROM clientes WHERE id_cliente = %s"
        parametros = (self.cod_cliente)
        respuesta = messagebox.askyesno(title="Confirmación", message="¿Quieres borrar este archivo permanente?")
        if respuesta:
            if conexion.ejecutarSQL(sql,parametros):
                messagebox.showinfo(title="Eliminar datos de los clientes", message="Datos del cliente eliminados  correctamente ...")
                clientes.limpiar(self)
                clientes.bloquear(self)
                clientes.cargarTabla(self)
            else:
                messagebox.showerror(title="Eliminar  datos de los clientes", message="Los datos del cliente no pueden ser elimininados ...")


        

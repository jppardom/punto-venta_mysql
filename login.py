from tkinter import *
from registrar import registrar
class login:
    def __init__ (self, vlogin):
        self.ventanaLogin = vlogin
        self.ventanaLogin.title("Login del sistema")
        self.frame = LabelFrame (self.ventanaLogin, text="Incio de sesión")
        self.frame.config(font=("Comic Sans MS", 18))
        self.frame.pack()
        
        self.lbl = Label (self.frame, text="Nombre de usuario")
        self.lbl.grid(column=1, row=1, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtUsuario = Entry(self.frame)
        self.txtUsuario.grid(column=2, row=1, padx=7, pady=7)
        self.txtUsuario.config(font=("Comic Sans MS", 14))

        self.lbl = Label (self.frame, text="Contraseña")
        self.lbl.grid(column=1, row=2, padx=7, pady=7)
        self.lbl.config(font=("Comic Sans MS", 14))

        self.txtPassword = Entry(self.frame)
        self.txtPassword.grid(column=2, row=2, padx=7, pady=7, sticky=E)
        self.txtPassword.config(font=("Comic Sans MS", 14), show="*")

        self.btnIngresar = Button(self.frame, text="INGRESAR", width=40)
        self.btnIngresar.grid(column=1, row=3, padx=7, pady=7, columnspan=2)
        self.btnIngresar.config(font=("Comic Sans MS", 14))

        self.btnRegistrar = Button(self.frame, text="REGISTRAR", width=40, command=self.registar)
        self.btnRegistrar.grid(column=1, row=4, padx=7, pady=7, columnspan=2)
        self.btnRegistrar.config(font=("Comic Sans MS", 14))

    def registar (self):
        self.ventanaLogin.destroy()
        registrar.__init__(self)   

if __name__ == "__main__":
    objTkinter = Tk()
    objLogin = login(objTkinter)
    objTkinter.mainloop()
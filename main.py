from tkinter import *
from tkinter import ttk as ttk
from usuarios import usuario
from tkinter import messagebox as MessageBox

root = Tk()
nombreUsuario = StringVar()
passwordUsuario = StringVar()
usuarios = []

def createGUI():

    # Ventana principal
    #root = Tk()
    root.title("Login usuario")

    # mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480, height=320)#, bg="lightblue")

    # textos y subtitulos
    titulo = Label(mainFrame, text="Login de usuario con Python", font=("Arial",24))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    nombreLabel = Label(mainFrame, text="Nombre: ")
    nombreLabel.grid(column=0,  row=1)
    passwordLabel = Label(mainFrame, text="Contraseña: ")
    passwordLabel.grid(column=0, row=2)

    # entradas de texto
    #nombreUsuario = StringVar()
    nombreUsuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    #passwordUsuario = StringVar()
    passwordUsuario.set("")
    passwordEntry = Entry(mainFrame, textvariable=passwordUsuario, show="*")
    passwordEntry.grid(column=1, row=2)

    # Botones
    iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar Sesión", command=iniciarSesion)
    iniciarSesionButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    registrarButton = ttk.Button(mainFrame, text="Registrar", command=registrarUsuario)
    registrarButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    root.mainloop()

def iniciarSesion():
    #global passwordUsuario
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            test = user.conectar(passwordUsuario.get())
            if test:
                MessageBox.showinfo("Conectado", f"Se inicio sesion en [{user.nombre}] con exito.")
            else:
                MessageBox.showerror("Error","Contraseña incorrecta.")
            break
    else:
        MessageBox.showerror("Error","No existen usuarios con ese nombre.")

def registrarUsuario():
    name = nombreUsuario.get()
    password = passwordUsuario.get()
    nuevoUsuario = usuario(name, password)
    usuarios.append(nuevoUsuario)
    MessageBox.showinfo("Registro exitoso", f"Se registró el usuario [{name}] con exito.")
    nombreUsuario.set("")
    passwordUsuario.set("")

    #root.mainloop()

if __name__ == "__main__":
    #user1 = usuario(inpout)
    user1 = usuario("Lucas", "1234")
    #usuarios = [user1]
    usuarios.append(user1)
    createGUI()


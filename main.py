# Importación de librerias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import re
import time
import sqlite3
import pandas as pd

# Importación de modulos
from usuarios import usuario
import tratamientoArchivos as ta

# Cargar lista de contraseñas débiles
with open('10k_most_common_passwords.txt') as f:
    weak_passwords = set(f.read().splitlines())

# Función para verificar si una contraseña es débil
def es_password_debil(password):
    return password in weak_passwords

# Función para verificar la validez de una contraseña según criterios de complejidad
def es_password_valido(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Función para crear la base de datos y la tabla de registros si no existen
def crear_bd():
    conn = sqlite3.connect('registros.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS REGISTROS
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NOMBRE TEXT NOT NULL,
                 APELLIDO TEXT NOT NULL,
                 NOMBRE_MATERIA TEXT NOT NULL,
                 NOTA TEXT NOT NULL);''')
    conn.close()

# Clase LoginApp: maneja la interfaz de inicio de sesión y registro de usuarios
class LoginApp:
    def __init__(self, root):
        # Atributos de la clase LoginApp
        self.root = root
        self.root.title("Login usuario")

        self.nombreUsuario = tk.StringVar()  # Variable para el nombre de usuario
        self.passwordUsuario = tk.StringVar()  # Variable para la contraseña
        self.usuarios = []  # Lista para almacenar usuarios
        self.intentos_fallidos = 0  # Contador de intentos fallidos

        self.create_gui()  # Crear la interfaz gráfica de usuario
        crear_bd()  # Crear la base de datos

    # Método para crear la interfaz gráfica de usuario
    def create_gui(self):
        mainFrame = tk.Frame(self.root)
        mainFrame.pack()
        mainFrame.config(width=480, height=320)

        # Etiquetas y campos de entrada
        titulo = tk.Label(mainFrame, text="Inicio de sesión", font=("Arial", 24))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

        subtitulo1 = tk.Label(mainFrame, text="Trabajo Práctico", font=("Arial", 16))
        subtitulo1.grid(column=0, row=1, padx=10, pady=5, columnspan=2)

        subtitulo2 = tk.Label(mainFrame, text="Diseño de sistemas 1", font=("Arial", 16))
        subtitulo2.grid(column=0, row=2, padx=10, pady=5, columnspan=2)

        nombreLabel = tk.Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=3, pady=10)
        passwordLabel = tk.Label(mainFrame, text="Contraseña: ")
        passwordLabel.grid(column=0, row=4, pady=10)

        self.nombreUsuario.set("")
        nombreEntry = tk.Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=3, pady=10)

        self.passwordUsuario.set("")
        passwordEntry = tk.Entry(mainFrame, textvariable=self.passwordUsuario, show="*")
        passwordEntry.grid(column=1, row=4, pady=10)

        # Botones de iniciar sesión y registrar
        iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciarSesionButton.grid(column=1, row=5, ipadx=5, ipady=5, padx=10, pady=10)

        registrarButton = ttk.Button(mainFrame, text="Registrar", command=self.registrar_usuario)
        registrarButton.grid(column=0, row=5, ipadx=5, ipady=5, padx=10, pady=10)

    # Método para iniciar sesión
    def iniciar_sesion(self):
        for user in self.usuarios:
            if user.nombre == self.nombreUsuario.get():
                if user.conectar(self.passwordUsuario.get()):
                    MessageBox.showinfo("Conectado", f"Se inició sesión en [{user.nombre}] con éxito.")
                    self.intentos_fallidos = 0  # Reiniciar contador de intentos fallidos
                    self.open_dashboard()
                else:
                    self.intentos_fallidos += 1
                    MessageBox.showerror("Error", "Contraseña incorrecta.")
                    print(f"Tiempo de espera: {self.intentos_fallidos * 2} segundos")
                    time.sleep(self.intentos_fallidos * 2)  # Incrementar el tiempo de espera
                break
        else:
            self.intentos_fallidos += 1
            MessageBox.showerror("Error", "No existen usuarios con ese nombre.")
            print(f"Tiempo de espera: {self.intentos_fallidos * 2} segundos")
            time.sleep(self.intentos_fallidos * 2)  # Incrementar el tiempo de espera

    # Método para registrar un nuevo usuario
    def registrar_usuario(self):
        name = self.nombreUsuario.get()
        password = self.passwordUsuario.get()

        if es_password_debil(password):
            MessageBox.showerror("Error", "La contraseña es demasiado débil. Elija otra.")
            return

        if not es_password_valido(password):
            MessageBox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, incluir letras mayúsculas, minúsculas, números y caracteres especiales.")
            return

        nuevoUsuario = usuario(name, password)
        self.usuarios.append(nuevoUsuario)
        MessageBox.showinfo("Registro exitoso", f"Se registró el usuario [{name}] con éxito.")
        self.nombreUsuario.set("")
        self.passwordUsuario.set("")

    # Método para abrir el dashboard
    def open_dashboard(self):
        self.root.withdraw()  # Esconder la ventana de login
        dashboard = tk.Toplevel(self.root)
        Dashboard(dashboard, self)

    # Método para limpiar los campos de entrada
    def clear_fields(self):
        self.nombreUsuario.set("")
        self.passwordUsuario.set("")

# Clase Dashboard: maneja la interfaz del panel principal después de iniciar sesión
class Dashboard:
    def __init__(self, root, login_app):
        # Atributos de la clase Dashboard
        self.root = root
        self.login_app = login_app
        self.root.title("Dashboard")
        
        self.archivo_seleccionado = None
        self.df = None  # DataFrame para almacenar el contenido cargado
        self.filas_seleccionadas = []  # Lista para almacenar las filas seleccionadas

        # Crear la interfaz del dashboard
        label = tk.Label(self.root, text="Registros", font=("Arial", 24))
        label.pack(padx=10, pady=10)

        seleccionar_button = ttk.Button(self.root, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        seleccionar_button.pack(padx=10, pady=10)

        cargar_button = ttk.Button(self.root, text="Cargar Archivo", command=self.cargar_archivo)
        cargar_button.pack(padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Nombre", "Apellido", "Nombre Materia", "Nota"), show='headings', selectmode='extended')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Nombre Materia", text="Nombre Materia")
        self.tree.heading("Nota", text="Nota")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        guardar_button = ttk.Button(self.root, text="Guardar Selección", command=self.guardar_seleccion)
        guardar_button.pack(padx=10, pady=10)

        ver_registros_button = ttk.Button(self.root, text="Ver Registros Guardados", command=self.ver_registros_guardados)
        ver_registros_button.pack(padx=10, pady=10)

        logout_button = ttk.Button(self.root, text="Cerrar Sesión", command=self.logout)
        logout_button.pack(padx=10, pady=10)

    # Método para seleccionar un archivo
    def seleccionar_archivo(self):
        self.archivo_seleccionado = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=(("Archivos PDF", "*.pdf"), ("Archivos Excel", "*.xlsx"), ("Archivos CSV", "*.csv"))
        )
        if self.archivo_seleccionado:
            MessageBox.showinfo("Archivo seleccionado", f"Has seleccionado el archivo: {self.archivo_seleccionado}")

    # Método para cargar el contenido del archivo seleccionado
    def cargar_archivo(self):
        if not self.archivo_seleccionado:
            MessageBox.showwarning("Advertencia", "Primero selecciona un archivo.")
        else:
            MessageBox.showinfo("Cargar archivo", f"Cargando archivo: {self.archivo_seleccionado}")
            self.mostrar_contenido_archivo()

    # Método para mostrar el contenido del archivo en el Treeview
    def mostrar_contenido_archivo(self):
        try:
            # Limpiar el contenido actual del treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            if self.archivo_seleccionado.endswith('.pdf'):
                texto = ta.extraer_datos_pdf(self.archivo_seleccionado)
                if texto:
                    self.df = ta.crear_dataframe(texto)
            elif self.archivo_seleccionado.endswith('.xlsx'):
                self.df = ta.extraer_datos_xlsx(self.archivo_seleccionado)
            elif self.archivo_seleccionado.endswith('.csv'):
                self.df = ta.extraer_datos_csv(self.archivo_seleccionado)

            if self.df is not None:
                for index, row in self.df.iterrows():
                    self.tree.insert("", tk.END, values=(row["Nombre"], row["Apellido"], row["Nombre Materia"], row["Nota"]))
        except Exception as e:
            MessageBox.showerror("Error", f"Ocurrió un error al cargar el archivo: {e}")

    # Método para guardar la selección en la base de datos
    def guardar_seleccion(self):
        selected_items = self.tree.selection()
        self.filas_seleccionadas = []
        for item in selected_items:
            row_values = self.tree.item(item, "values")
            self.filas_seleccionadas.append(row_values)
        
        self.guardar_en_bd()
        MessageBox.showinfo("Guardar Selección", f"Se han guardado {len(self.filas_seleccionadas)} filas seleccionadas.")

    # Método para guardar los registros seleccionados en la base de datos
    def guardar_en_bd(self):
        conn = sqlite3.connect('registros.db')
        c = conn.cursor()
        for row in self.filas_seleccionadas:
            c.execute("INSERT INTO REGISTROS (NOMBRE, APELLIDO, NOMBRE_MATERIA, NOTA) VALUES (?, ?, ?, ?)", row)
        conn.commit()
        conn.close()

    # Método para ver los registros guardados
    def ver_registros_guardados(self):
        registros_ventana = tk.Toplevel(self.root)
        registros_ventana.title("Registros Guardados")

        tree = ttk.Treeview(registros_ventana, columns=("Nombre", "Apellido", "Nombre Materia", "Nota"), show='headings')
        tree.heading("Nombre", text="Nombre")
        tree.heading("Apellido", text="Apellido")
        tree.heading("Nombre Materia", text="Nombre Materia")
        tree.heading("Nota", text="Nota")
        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        for row in self.filas_seleccionadas:
            tree.insert("", tk.END, values=row)

    # Método para cerrar sesión y volver a la ventana de login
    def logout(self):
        self.root.destroy()  # Cierra la ventana del dashboard
        self.login_app.clear_fields()
        main_window.deiconify()  # Muestra de nuevo la ventana de login

# Punto de entrada principal del programa
if __name__ == "__main__":
    main_window = tk.Tk()
    app = LoginApp(main_window)
    user1 = usuario("Lucas", "1234")
    app.usuarios.append(user1)
    main_window.mainloop()











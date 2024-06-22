class usuario():
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.conectado = False
        self.intentos = 3

    def conectar(self, password=None):
        if password is None:
            myPassword = input("Ingrese su contraseña: ")
        else:
            myPassword = password
        if myPassword == self.password:
            print("Se ha conectado con éxito")
            self.conectado = True
            return True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, inténtelo de nuevo...")
                if password is not None:
                    return False
                print("Intentos restantes:", self.intentos)
            else:
                print("Error, no se pudo iniciar sesión.")
                print("Adiós.")
                return False

    def desconectar(self):
        if self.conectado:
            print("Se cerró sesión con éxito")
            self.conectado = False
        else:
            print("Error, no inició sesión")

    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else:
            conect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

    

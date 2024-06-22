class usuario():
    def __init__(self,nombre,password):
        self.nombre = nombre
        self.password = password

        self.conectado = False
        self.intentos = 3

        #usuario.numUsuarios += 1

    def conectar(self, password = None):
        if password == None:
            myPassword = input("Ingrese su contraseña: ")
        else:
            myPassword = password
        if myPassword == self.password:
            print("Se ha conectado con exito")
            self.conectado = True
            return True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, intentelo devuelta...")
                #print("Intentos restantes:", self.intentos)
                if password != None:
                #self.conectar()
                    return False
                print("Intentos restantes:", self.intentos)
            else:
                print("Error, no se pudo iniciar sesión.")
                print("Adios.")
    
    def desconectar(self):
        if self.conectado:
            print("Se cerro sesión con exito")
            self.conectado = False
        else:
            print("Error, no inicio sesión")

    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else:
            conect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"
    

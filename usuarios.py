# Clase usuario: representa a un usuario del sistema
class usuario():
    # Método constructor (__init__): inicializa los atributos de la clase usuario
    def __init__(self, nombre, password):
        self.nombre = nombre  # Atributo: nombre del usuario
        self.password = password  # Atributo: contraseña del usuario
        self.conectado = False  # Atributo: estado de conexión del usuario (False por defecto)
        self.intentos = 3  # Atributo: número de intentos permitidos para iniciar sesión

    # Método conectar: verifica la contraseña y conecta al usuario si es correcta
    def conectar(self, password=None):
        if password is None:
            myPassword = input("Ingrese su contraseña: ")  # Solicita la contraseña si no se proporciona
        else:
            myPassword = password
        if myPassword == self.password:  # Verifica si la contraseña es correcta
            print("Se ha conectado con éxito")
            self.conectado = True  # Cambia el estado de conexión a True
            return True
        else:
            self.intentos -= 1  # Decrementa el número de intentos permitidos
            if self.intentos > 0:
                print("Contraseña incorrecta, inténtelo de nuevo...")
                if password is not None:
                    return False
                print("Intentos restantes:", self.intentos)
            else:
                print("Error, no se pudo iniciar sesión.")
                print("Adiós.")
                return False

    # Método desconectar: desconecta al usuario si está conectado
    def desconectar(self):
        if self.conectado:  # Verifica si el usuario está conectado
            print("Se cerró sesión con éxito")
            self.conectado = False  # Cambia el estado de conexión a False
        else:
            print("Error, no inició sesión")

    # Método __str__: devuelve una representación en cadena del estado del usuario
    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else:
            conect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

    

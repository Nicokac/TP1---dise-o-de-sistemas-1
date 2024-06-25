Este TP fue realizado por: Lucas Sanchez y Nicolás Kachuk
# Sistema de Registro de Usuarios y Manejo de Archivos

## Descripción

Este es un sistema de inicio de sesión y registro de usuarios desarrollado en Python, utilizando la librería Tkinter para la interfaz gráfica. Los usuarios pueden registrarse, iniciar sesión y cargar archivos en formato .PDF, .XLS y .CSV. El contenido de los archivos cargados se visualiza en la aplicación y se puede guardar en una base de datos SQLite.

## Características

- **Registro de Usuarios**: Permite a los usuarios registrarse con un nombre y una contraseña. La contraseña debe cumplir con requisitos como tener mínimo 8 caracteres, entre los cuales debe tener números y caracteres especiales.
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión con su nombre y contraseña registrados.
- **Carga de Archivos**: Los usuarios pueden cargar archivos .PDF, .XLS y .CSV y visualizar su contenido.
- **Visualización de Datos**: El contenido de los archivos se muestra en una interfaz de tabla.
- **Persistencia de Datos**: Los registros seleccionados se pueden guardar en una base de datos SQLite.

## Requisitos

- Python 3.x
- Tkinter (incluido con Python)
- Pandas
- PyPDF2
- openpyxl

## Instalación

### Clonar el repositorio:

-  ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

### **Crear entorno virtual:**
-  ```bash
   python -m venv venv

### Activar entorno virtual:
-  ```bash
   venv\Scripts\activate

### Instalar dependencias:
-  ```bash
   pip install -r requirements.txt

### Ejecutar la aplicación:
-  ```bash
   python main.py
 
## Uso:

### Registro de Usuario:
- Ingrese un nombre de usuario y una contraseña.
- Haga clic en el botón "Registrar".

### Inicio de Sesión:
- Ingrese su nombre de usuario y contraseña registrados.
- Haga clic en el botón "Iniciar Sesión".

### Carga de Archivos:
- En la ventana del dashboard, haga clic en "Seleccionar Archivo" y elija un archivo PDF, XLS o CSV.
- Haga clic en "Cargar Archivo" para visualizar su contenido.

### Guardar Registros:
- Seleccione las filas que desea guardar.
- Haga clic en "Guardar Selección" para almacenar los registros en la base de datos.

### Ver Registros Guardados:
- Haga clic en "Ver Registros Guardados" para visualizar los registros almacenados.

## Estructura del Proyecto:

TP1 - DISEÑO DE SISTEMAS 1
│
├── main.py
├── usuarios.py
├── tratamientoArchivos.py
├── registros.db
├── 10k_most_common_passwords.txt
├── prueba.csv
├── prueba.pdf
├── prueba.xlsx
├── DER.plantuml
├── DiagramadeClases.plantuml
└── README.md



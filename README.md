# Sistema de Registro de Usuarios y Manejo de Archivos

## Descripción

Este es un sistema de inicio de sesión y registro de usuarios desarrollado en Python, utilizando la librería Tkinter para la interfaz gráfica. Los usuarios pueden registrarse, iniciar sesión y cargar archivos en formato .PDF, .XLXS y .CSV. 
El contenido de los archivos cargados se visualiza en la aplicación y se puede guardar en una base de datos SQLite.

## Características

- **Registro de Usuarios**: Permite a los usuarios registrarse con un nombre y una contraseña. La contraseña debe cumplir con requisitos como tener mínimo 8 caracteres, entre de los cuales debe tener números y caracteres especiales.
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión con su nombre y contraseña registrados.
- **Carga de Archivos**: Los usuarios pueden cargar archivos .PDF, .XLXS y .CSV y visualizar su contenido.
- **Visualización de Datos**: El contenido de los archivos se muestra en una interfaz de tabla.
- **Persistencia de Datos**: Los registros seleccionados se pueden guardar en una base de datos SQLite.

## Requisitos

- Python 3.x
- Tkinter (incluido con Python)
- Pandas
- PyPDF2
- openpyxl

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

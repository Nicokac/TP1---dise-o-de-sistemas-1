import pandas as pd
from PyPDF2 import PdfReader
import openpyxl

def extraer_datos_pdf(nombre_archivo):
    try:
        lector = PdfReader(nombre_archivo)
        if len(lector.pages) > 0:
            pagina = lector.pages[0]
            texto = pagina.extract_text()
            if texto:
                return texto
            else:
                print("No se pudo extraer el texto de la primera página.")
        else:
            print("El archivo PDF no contiene páginas.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return None

def crear_dataframe(texto):
    lineas = texto.strip().split('\n')
    columnas = ['Nombre', 'Apellido', 'Nombre Materia', 'Nota']
    datos = [linea.rsplit(maxsplit=4) for linea in lineas[1:]]
    df = pd.DataFrame(datos, columns=columnas)
    return df

def extraer_datos_xlsx(nombre_archivo):
    try:
        df = pd.read_excel(nombre_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return None

def extraer_datos_csv(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return None

def main():
    # Extraer texto del PDF
    texto_extraido = extraer_datos_pdf('prueba.pdf')
    if texto_extraido:
        df_pdf = crear_dataframe(texto_extraido)
        print("Archivo .pdf extraído")
        print(df_pdf)

    # Extraer datos del archivo .xlsx
    df_xlsx = extraer_datos_xlsx('prueba.xlsx')
    if df_xlsx is not None:
        print("Archivo .xlsx extraído")
        print(df_xlsx)
    
    # Extraer datos del archivo .csv
    df_csv = extraer_datos_csv('prueba.csv')
    if df_csv is not None:
        print("Archivo .csv extraído")
        print(df_csv)

if __name__ == "__main__":
    main()

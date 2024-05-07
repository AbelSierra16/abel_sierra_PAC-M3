from cowsay import cowsay
import os


def menuInicial():
    print("|======================================|")
    print("|      El Libro de las acepciones      |")
    print("|======================================|")
    print("1. Añadir palabra y accepción")
    print("2. Mostrar palabras y accepciones")
    print("3. Modificar palabra o accepción")
    print("4. Eliminar palabra o accepción")
    print("5. Salir")
    print("========================================")
    """Printa el menu Inicial"""


def menuAfegir():
    os.system('cls')
    print("|======================================|")
    print("|       Añadir Nuevas acpeciones       |")
    print("|======================================|\n")
    """Prnta el menu de añadir nuevas palabras/acepciones"""
 
def menuMostrar():
    os.system('cls')
    print("|======================================|")
    print("|    Palabras y acepciones actuales    |")
    print("|======================================|\n")
    """Prnta el menu para mostrar las palabras y acepciones actuales"""

def mostrarParaules(diccionari):
    
    diccionari_str = "\n".join(f"{k}: {v}\n" for k, v in diccionari.items())
    print(cowsay(diccionari_str))
    """Muestra el diccionario de palabras formateado a string mediante la libreria cowsay"""

    
    
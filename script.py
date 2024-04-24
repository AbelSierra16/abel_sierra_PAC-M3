from cowsay import cowsay
import os

def mostrarMenu():
    print("========================================")
    print("= El Llibre de les Accepcions          =")
    print("========================================")
    print("1. Añadir palabra y accepción")
    print("2. Mostrar palabras y accepciones")
    print("3. Modificar palabra o accepción")
    print("4. Eliminar palabra o accepción")
    print("5. Salir")
    print("========================================")



#def main():
diccionari = {}

while True:

    os.system('cls')
    mostrarMenu()

    eleccion = int(input('Elige una opcion: '))

    if eleccion == 1:
        palabra  = input('Introduce la palabra: ')
        accepcion = input('Introduce l''acepcion: ')

        diccionari.update({palabra:accepcion})

    elif eleccion == 2:
        print(cowsay(str(diccionari)))
        input()

    elif eleccion == 3:
        modificar = int(input('Que quieres modificar?(1. Palabra, 2. Acepcion) '))

        if modificar == 1:
            auxiliar = input('Introdueix la nova palabra ')
            diccionari.update({auxiliar:accepcion})
            print('Palabra modificada correctamente')
            input()
        else:
            auxiliar = input('Introduce la nueva acepcion')
            diccionari.update({palabra:auxiliar})
            
        

    
    
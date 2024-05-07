from funciones import *


diccionari ={}

palabra = ""
entrada = {}

valorEntrada = ""
clauEntrada  = ""

#def main():


while True:

    os.system('cls')
    menuInicial()

    eleccion = int(input('Elige una opcion: '))

    if eleccion == 1:
        menuAfegir()
        palabra = input('Introdueix una palabra: ')
        if(palabra in diccionari):
            print('No pots afegir una paraula ja existent')

        else:
            clauEntrada = input('Introdueix la clau de la palabra: ')
            valorEntrada = input('Introdueix el valor de la clau: ')

            entrada = {clauEntrada:valorEntrada}

            diccionari.update({palabra:entrada})

    elif eleccion == 2:
        menuMostrar()
        mostrarParaules(diccionari)
        input('Presiona para continuar')

    elif eleccion == 3:
        menuMostrar()
        mostrarParaules(diccionari)
        modificar = input('Que palabra quieres modificar : ')

        if modificar in diccionari:
            clauEntrada = input('Introdueix la clau de la palabra: ')
            valorEntrada = input('Introdueix el valor de la clau: ')
            entrada = {clauEntrada:valorEntrada}

            auxiliar = diccionari[modificar]

            auxiliar.update(entrada)
            diccionari.update({palabra:auxiliar})

    elif eleccion == 4:
        menuMostrar()
        mostrarParaules(diccionari)
        eliminar = input('Que palabra quieres eliminar? ')

        if eliminar in diccionari:
            del diccionari[eliminar]
            print('Palabra eliminada con éxito.')
        else:
            print('La palabra que quieres eliminar no existe en el diccionario.')
    elif eleccion == 5:
        print('Tancant Programa')
        input('Presiona para continuar')
        break
    else:
        print('Opcio no valida')
        input('Presiona para continuar')
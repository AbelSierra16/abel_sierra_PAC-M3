from funciones import *




#def main():
diccionari = {}

while True:

    os.system('cls')
    menuInicial()

    eleccion = int(input('Elige una opcion: '))

    if eleccion == 1:
        menuAfegir()
        palabra  = input('Introduce la palabra: ')
        if(palabra in diccionari):
            print('No pots afegir una paraula ja existent')

        else:
            accepcion = input('Introduce l''acepcion: ')
            diccionari.update({palabra:accepcion})

    elif eleccion == 2:
        mostrarParaules(diccionari)
        input('Presiona para continuar')

    elif eleccion == 3:
        mostrarParaules(diccionari)
        modificar = input('Que palabra quieres modificar? ')

        if modificar in diccionari:
            eleccionMod = input('Quieres cambiar la palabra(1) o acepcion(2)?')

            if eleccionMod == '1':
                nueva_palabra = input('Introduce la Palabra modificada: ')
                diccionari[nueva_palabra] = diccionari.pop(modificar)
            elif eleccionMod == '2':
                nueva_acepcion = input('Introduce la nueva acepcion: ')
                diccionari[modificar] = nueva_acepcion
        else:
            print('La palabra que quieres modificar no existe en el diccionario.')

    elif eleccion == 4:
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
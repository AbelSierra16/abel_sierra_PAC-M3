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
        mostrarParaules()
        modificar = int(input('Que palabra quieres modificar? '))

        if modificar in diccionari:
            eleccionMod = input('Quieres cambiar la palabra(1) o acepcion(2)?')

            if eleccionMod == 1:
                aux = input('Introduce la Palabra modificada: ')
           
        else:
            auxiliar = input('Introduce la nueva acepcion')
            diccionari.update({palabra:auxiliar})
            
        

    
    
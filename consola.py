# -*- coding: utf-8 -*-

#TODO: importar el módulo

def ejecutar_dar_clase_numero()->None:
    """Esta funcion permite ejecutar la función dar_clase_numero"""
    
    # TODO: implementar la función """  
    
def ejecutar_PUM()->None:
    """Esta funcion permite ejecutar el juego del PUM  """
    
    # TODO: implementar la función """  
    
def ejecutar_adivinar_numero()->None: 
    """Esta funcion permite ejecutar la función que haya programado para adivinar un numero de 1 a 9. """
    
    # TODO: implementar la función """
    

def mostrar_menu()->bool:
    print("1. Dar clase de un número")
    print("2. Jugar PUM")
    print("3. Adivinar un número de 1 a 10")
    print("4. Salir")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        print("opc1")
    elif opcion_elegida == "2":
        print("opc2")
    elif opcion_elegida == "3":
        print("opc3")
    elif opcion_elegida == "4":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

def iniciar_aplicacion()->None:
    """
    Esta función mantiene el programa funcionando hasta que el usuario seleccione la opción para salir.
    La función primero debe mostrar el menú de opciones usando la función mostrar_menu().
    A continuación, debe solicitarle al usuario una opción.
    Según lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccionó la opción de Salir, la función debe terminar su ejecución para que el programa pueda terminar.
    Si el usuario seleccionó cualquier otra opción, después de ejecutar la opción seleccionada se debe volver
    a mostrar el menú de opciones y se debe repetir el proceso.
    """
    ejecutando = True
    while ejecutando:

        ejecutando = mostrar_menu()
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

iniciar_aplicacion()

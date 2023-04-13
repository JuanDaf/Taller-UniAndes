# -*- coding: utf-8 -*-

import modulo as md

def ejecutar_dar_clase_numero()->None:
    """Esta funcion permite ejecutar la función dar_clase_numero"""
    
    print(md.dar_clase_numero(int(input("Ingresa el numero: "))) ) 
    
def ejecutar_PUM()->None:
    """Esta funcion permite ejecutar el juego del PUM  """
    
    md.jugar_PUM(int(input("Ingresa el numero de jugadores: ")), int(input("Ingresa el numero escogido para el PUM: ")))  
    
def ejecutar_adivinar_numero()->None: 
    """Esta funcion permite ejecutar la función que haya programado para adivinar un numero de 1 a 9. """
    
    print(md.adivinar_numero(int(input("Ingresa el numero: "))))
    

def mostrar_menu()->bool:
    print("1. Dar clase de un número")
    print("2. Jugar PUM")
    print("3. Adivinar un número de 1 a 10")
    print("4. Salir")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_dar_clase_numero()
    elif opcion_elegida == "2":
        ejecutar_PUM()
    elif opcion_elegida == "3":
        ejecutar_adivinar_numero()
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

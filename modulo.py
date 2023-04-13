# -*- coding: utf-8 -*-


import random 

def dar_clase_numero(numero:int)->str:
    """ Esta función permite saber si un numero 
    entero es un rey par, un noble par, guerrero par y rebelde impar. 
    Parámetros:
        numero(int): numero ingresado por el usuario.
    Retorno:
        Str: Informando al usuario con la clase a la cual pertenece el número.
    """
    centinela=False
    num=0
    numero_inicial=numero

    while centinela==False:
        if numero==0:
            centinela=True
        else:
            dig=numero%10
            num+=dig
            numero//=10     
            
    par_1=numero_inicial%2
    par_2=num%2
    print(par_1,par_2)
    respuesta=str("")
    if par_1==0 and par_2==0 :
        respuesta=str("Rey Par")
    elif par_1!=0 and par_2==0:
        respuesta=str("Noble Par")
    elif par_1==0 and par_2!=0:
        respuesta=str("Guerreo Par")
    elif par_1!=0 and par_2!=0:
        respuesta=str("Reblede Impar")
    return respuesta

  
  
            

def jugar_PUM(jugadores: int, numero: int)-> None:
    """
    Simula el juego del PUM.
    Parámetros:
        jugadores: cantidad de jugadores
        numero: número escogido para el PUM 
    Retorno:
        No retorna nada ya que imprime por pantalla el desarrollo del juego
    """
    x =  0
    jugad = 0
    mult = 0
    temp = 0
    while(x != 500):
        x = x + 1
        jugad = jugad + 1 
        while(mult <= 500):
            mult = mult + numero
            if(x == mult):
               print("Jugador: ",jugad, "Jugada: ", "PUM" )   
               temp = 1         
        mult = 0
        if(temp == 1):
            temp = 0
        else:
            print("Jugador: ",jugad, "Jugada: ", x )
            
        if(jugad == jugadores):
            jugad = 0


##print(jugar_PUM(5,9))

def adivinar_numero(numero:int)->str:
    """ Esta función permite adivinar un numero entre 1 y 9.
    Parámetros:
        numero(int): numero ingresado por el usuario.
    Retorno:
        Str: Informando al usuario cuando adivino el número.
        Recuerde que el programa continua funcionando hasta el usuario 
        adivina el número escogido por el sistema (este número es 
        dado mendiante la funcion random.randint)
    """
    numero_generado= random.randint(1, 9)
    centinela=False
    while centinela==False:
        if numero_generado==numero:
            centinela=True
            numero_ingresado= ("El numero ingresado fue el correcto")
        elif numero_generado!=numero:
            numero_ingresado=  ("Nuemero Incorrecto")
            numero= int(input("Ingrese un nuevo numero "))    
    return numero_ingresado

##print(adivinar_numero(1))
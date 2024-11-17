'''
#! Isai Almeraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Interaccion con el usuario(Main)
'''
#? Librerias
import random as rd #* Libreria para generar numeros aleatorios

#? LLamadas a Clases

#? Creacion de objetos

#? Funciones
def menu_principal(): #* Muestra el menu principal del juego
    print("||--------Opciones para Pokemon---------||")
    print("|| 1 -> Crear Pokemon enemigos          ||")
    print("|| 2 -> Simular Batalla                 ||")
    print("|| 3 -> Mostrar Pokemone Capturados     ||")
    print("|| 4 -> Actulizar Detalles devPokemon   ||")
    print("|| 5 -> Entrenar Pokemon                ||")
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||")
    
    opcion = int(input("\nIngrese opcion: "))
    return opcion

def Detalles_Pokemon(): #* Muestra los detalles de un Pokemon
    pass

def menu_elegir_pokemon():  #* Muestra el menu para elegir el pokemon inicial
    print("||------------------Menu------------------||")
    print("||        Aun no tienes un Pokemon        ||")
    print("||    Elige a tu pokemon para iniciar!    ||")
    print("||****************************************||")
    print("|| 1 -> Squirtle(Agua)                    ||")
    print("|| 2 -> Charmander(Fuego)                 ||")
    print("|| 3 -> Shinx(Electrico)                  ||")
    print("|| 4 -> Bulbasaur(Hierba)                 ||")
    print("||----------------------------------------||")
    
    while True:
        
        opc = int(input("\nIngrese opcion: "))
        
        if opc == 1:
            # muestra los detalles del pokemon y pregunta si esta seguro de elegitlo
            # si esta seguro se crea el objeto pokemon y se retorna
            pass
    
        elif opc == 2:
            # muestra los detalles del pokemon y pregunta si esta seguro de elegitlo
            # si esta seguro se crea el objeto pokemon y se retorna
            pass
        
        elif opc == 3:
            # muestra los detalles del pokemon y pregunta si esta seguro de elegitlo
            # si esta seguro se crea el objeto pokemon y se retorna
            pass
        
        elif opc == 4:
            # muestra los detalles del pokemon y pregunta si esta seguro de elegitlo
            # si esta seguro se crea el objeto pokemon y se retorna
            pass
        
        else:
            print("\nOpcion no valida!\n")
            continue
        

def Menu_Entrenar_Pokemon(): #* Muestra el menu para entrenar a un Pokemon
    pass

def Entrenar_Pokemon(): #* Entrena los niveles de ataque, defensa y vida de un Pokemon
    pass

def Menu_Actualizar_Pokemon(): #* Muestra el menu para actualizar los detalles de un Pokemon
    pass

def Actualizar_Pokemon(): #* Actualiza los detalles de un Pokemon individualmente
    pass

def Crear_Pokemon_Enemigo(): #* Crea un Pokemon enemigo aleatorio
    pass

def Batalla_Pokemon(): #* Simula una batalla entre dos Pokemones
    pass

def Pokemones_Capturados(): #* Muestra la lista de Pokemones capturados
    pass



def Saludo_Inicial():#? Saluda al usuario por primera vez en el juego, mostrando el nombre del juego y una breve descripcion
    print("\n||------------------------------Examen-Pokemon------------------------------||\n")
    nombre = input("Ingrese su nombre: ")
    print(f"\nBienvenido al Juego {nombre}!")
    print("Este es un Juego de Pokemon, donde podras capturar, entrenar a tus propios Pokemon y tener \nbatallas con otros Pokemon salvajes!")
    print("\n||--------------------------------------------------------------------------||\n")

#! Codigo Principal

#? Variales
Lista_Pokemones = [] #* Lista para almacenar los Pokemones capturados

#? Saludo al usuario
Saludo_Inicial() #* Saluda al usuario por primera vez en el juego, mostrando el nombre del juego y una breve descripcion

#? Elegir Pokemos Inicial
#Pokemon_Inicial = menu_elegir_pokemon() #* Muestra el menu para elegir el pokemon inicial

#? Ciclo para interactuar con el usuario
while True:
    
    opc = menu_principal() #* Muestra el menu principal del juego 

    if opc == 9:
        # Mandar mensaje resumiendo cuantos pokemones capturo, cuantas derrotas tuvo y cuantas victorias
        print("\nSaliendo...\nGracias por usar el programa!")
        break  #* Termina el programa al elegir la opción de salida en el menú principal
    
    elif opc == 1: #* Metodo para crear un nuevo Pokemon enemigo
        # crear_pokemon_enemigo()
        pass
    
    elif opc == 2: #* Metodo para Simmular una batalla entre dos Pokemones
        # se debe llama a la funcion batalla_pokemon()
        # en la funcion se debe elegir un pokemon enemigo aleatorio, se mostraran sus detalles y
        # se mostraran tus pokemones capturados para elegir uno para la batalla
        #si ganas podras capturar al pokemon enemigo
        #-------------------------------------------------------------------------
        # si ya venciste a los 4 pokemon predefinidos deberasa crear un nuevo pokemon enemigo
        pass
    
    elif opc == 3: #* Mostrar Lista de Pokemones Capturados y sus detalels
        # pokemones_capturados()
        # Ciclo para mostrar detalles de cada pokemon y un conteo de cuantos son |detalles_pokemon()
        pass
    
    elif opc == 4:#* Metodo para Entrenar los niveles de ataque, defensa y vida Pokemon
        # menu_entrenar_pokemon()
        # se debe elegir un pokemon para entrenar y se mostraran sus detalles manualmente
        pass
    
    elif opc == 5: #* Metodo para Actualizar los niveles de ataque, defensa y viada Pokemon individualmente
        # actualizar_pokemon()
        # se debe elegir un pokemon para entrenar y se mostraran sus detalles
        pass
    
    else:
        print("\nOpcion no valida!\n")

print("\n||--------------------------------------------------------------------------||\n")

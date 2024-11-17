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
def Detalles_Pokemon(): #? Muestra los detalles de un Pokemon | Recibe un objeto Pokemon para mostrar sus detalles 
    #TODO: necesita un objeto pokemon para mostrar sus detalles (Falta ezequiel y sofia)
    pass

def Pokemones_Capturados(): #? Muestra la lista de Pokemones capturados
    
    for i in Lista_Pokemones: #* Ciclo para mostrar una lista de los Pokemones capturados
        print(Detalles_Pokemon(i)) #* Muestra los detalles de cada Pokemon capturado
        
def menu_principal(): #? Muestra el menu principal del juego
    
    print("\n||--------Opciones para Pokemon---------||")
    print("|| 1 -> Crear Pokemon enemigos          ||")
    print("|| 2 -> Simular Batalla                 ||")
    print("|| 3 -> Mostrar Pokemone Capturados     ||")
    print("|| 4 -> Actulizar Detalles devPokemon   ||")
    print("|| 5 -> Entrenar Pokemon                ||")
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||\n")
    
    opcion = int(input("\nIngrese opcion: "))
    return opcion

def menu_elegir_pokemon():  #? Muestra el menu para elegir el pokemon inicial
    
    print("\n||------------------Menu------------------||")
    print("||        Aun no tienes un Pokemon        ||")
    print("||    Elige a tu pokemon para iniciar!    ||")
    print("||****************************************||")
    print("|| 1 -> Squirtle(Agua)                    ||")
    print("|| 2 -> Charmander(Fuego)                 ||")
    print("|| 3 -> Shinx(Electrico)                  ||")
    print("|| 4 -> Bulbasaur(Hierba)                 ||")
    print("||----------------------------------------||\n")
    
    while True:
        
        opc = int(input("\nIngrese opcion: "))
        
        if opc == 1:
            Detalles_Pokemon() #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                print("\nHas elegido a Squirtle!\n")
                return "Squirtle" #TODO: Retorna el objeto Pokemon elegido
            else:
                continue
    
        elif opc == 2:
            Detalles_Pokemon() #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                print("\nHas elegido a Charmander!\n")
                return "Charmander" #TODO: Retorna el objeto Pokemon elegido
            else:
                continue
        
        elif opc == 3:
            Detalles_Pokemon() #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                print("\nHas elegido a Shinx!\n")
                return "Shinx" #TODO: Retorna el objeto Pokemon elegido
            else:
                continue
        
        elif opc == 4:
            Detalles_Pokemon() #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                print("\nHas elegido a Bulbasaur!\n")
                return "Bulbasaur" #TODO: Retorna el objeto Pokemon elegido
            else:
                continue
        
        else:
            print("\nOpcion no valida!\n")
            continue
        

def Menu_Entrenar_Pokemon(): #? Muestra el menu para entrenar a un Pokemon
    
    Pokemones_Capturados() #* Muestra la lista de Pokemones capturados
    
    pokemon_en_entrenamiento = input("Que pokemon deseas entrenar?") #* Pregunta al usuario que Pokemon desea entrenar
    
    print("\n||--------Opciones para Pokemon---------||")
    print("|| 1 -> Entrenar Vida                   ||")
    print("|| 2 -> Entrenar Ataque                 ||")
    print("|| 3 -> Entrenar Defensa                ||")
    print("|| 4 -> Entrenar                        ||") #TODO no se si se necesita entrenar el ataque especial(Falta ezequiel y sofia)
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||\n")
    
    while True:
        
        opc = int(input("\nIngrese opcion: "))
        
        if opc == 1: #* Metodo para entrenar la vida de un Pokemon
            #TODO: subir_Vida(Nombre del objeto Pokemon) 
            pass
    
        elif opc == 2:  #* Metodo para entrenar el ataque de un Pokemon
            #TODO: subir_Ataque(Nombre del objeto Pokemon))
            pass
        
        elif opc == 3:  #* Metodo para entrenar la defensa de un Pokemon
            #TODO: subir_Defensa(Nombre del objeto Pokemon))
            pass
        
        elif opc == 4:  #* Metodo pendiente 
            pass
        
        else:
            print("\nOpcion no valida!\n")
            continue

def Menu_Actualizar_Pokemon(): #? Muestra el menu para actualizar los detalles de un Pokemon
    
    Pokemones_Capturados() #* Muestra la lista de Pokemones capturados
    
    pokemon_para_actualizar = input("Que pokemon deseas actualizar?") #* Pregunta al usuario que Pokemon desea entrenar
    
    print("\n||--------Opciones para Pokemon---------||")
    print("|| 1 -> actualizar Vida                   ||")
    print("|| 2 -> actualizar Ataque                 ||")
    print("|| 3 -> actualizar Defensa                ||")
    print("|| 4 -> actualizar                        ||") #TODO no se si se necesita entrenar el ataque especial(Falta ezequiel y sofia)
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||\n")
    
    while True:
        
        opc = int(input("\nIngrese opcion: "))
        
        if opc == 1: #* Metodo para entrenar la vida de un Pokemon
            #TODO: actualizar_Vida(Nombre del objeto Pokemon) 
            pass
    
        elif opc == 2:  #* Metodo para entrenar el ataque de un Pokemon
            #TODO: actualizar_Ataque(Nombre del objeto Pokemon))
            pass
        
        elif opc == 3:  #* Metodo para entrenar la defensa de un Pokemon
            #TODO: actualizar_Defensa(Nombre del objeto Pokemon))
            pass
        
        elif opc == 4:  #* Metodo pendiente 
            pass
        
        else:
            print("\nOpcion no valida!\n")
            continue

def Crear_Pokemon_Enemigo(): #? Crea un Pokemon enemigo aleatorio
    pass #TODO: falta crear este metodo

def Capturar_Pokemon(): #? Captura un Pokemon enemigo
    pass #TODO: falta crear este metodo

def Batalla_Pokemon(): #? Simula una batalla entre dos Pokemones
    pass #TODO: falta crear este metodo




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


#TODO: Falta crear los metodos de las siguientes funciones:
#? Crear_Pokemon_Enemigo()
#? Capturar_Pokemon()
#? Batalla_Pokemon()

#TODO: falta agregar funcionalidades a las siguientes funciones(falta ezequiel y sofia):
#? Detalles_Pokemon()
#? Menu_Entrenar_Pokemon()
#? Menu_Actualizar_Pokemon()
#? menu_elegir_pokemon()

#TODO: Falta agregar la funciones a el Main switch
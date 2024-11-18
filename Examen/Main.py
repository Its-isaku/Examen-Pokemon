'''
#! Isai Almeraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Interaccion con el usuario(Main)
'''
#? Librerias
import random as rd
from Examen import Agua #* Libreria para generar numeros aleatorios
from Examen import Electro #* Libreria para generar numeros aleatorios
from Examen import Fuego #* Libreria para generar numeros aleatorios
from Examen import Hierba #* Libreria para generar numeros

#? Variales
lista_pokemones_iniciales = [] #* Lista para almacenar los Pokemones iniciales(Para elegir uno)
lista_pokemones_enemigos = [] #* Lista para almacenar los Pokemones enemigos
lista_pokemones = [] #* Lista para almacenar los Pokemones capturados

#? LLamadas a Clases

#! Creacion de Objetos
#? Creacion de Pokemones Principales
lista_pokemones_iniciales.add(Squirtel = Agua(nombre="Squirtel", vida=100, ataque=10, defensa=10, ataque_agua="Hidrobomba")) #* Creacion de un objeto de tipo Agua
lista_pokemones_iniciales.add(Charmander = Fuego(nombre="Charmander", vida=100, ataque=10, defensa=10, ataque_fuego="Lanzallamas")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_iniciales.add(Shinx = Electro(nombre="Shinx", vida=100, ataque=10, defensa=10, ataque_electro="Rayo")) #* Creacion de un objeto de tipo Electro
lista_pokemones_iniciales.add(Bulbasaur = Hierba(nombre="Bulbasaur", vida=100, ataque=10, defensa=10, ataque_hierba="Latigo Cepa")) #* Creacion de un objeto de tipo Hierba

#? Creacion de Pokemones Enemigos
lista_pokemones_enemigos.add(Vulpix = Fuego(nombre="Vulpix", vida=250, ataque=40, defensa=30, ataque_agua="Hidrobomba")) #* Creacion de un objeto de tipo Agua
lista_pokemones_enemigos.add(Golduck = Agua(nombre="Golduck", vida=350, ataque=30, defensa=30, ataque_fuego="Lanzallamas")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_enemigos.add(Electrabuzz = Electro(nombre="Electrabuzz", vida=450, ataque=50, defensa=60, ataque_electro="Rayo")) #* Creacion de un objeto de tipo Electro
lista_pokemones_enemigos.add(Gloom = Hierba(nombre="Gloom", vida=150, ataque=20, defensa=25, ataque_hierba="Latigo Cepa")) #* Creacion de un objeto de tipo Hierba

#? Funciones

#? Metodo para mostrar los pokemones capturados
def Pokemones_Capturados(): #? Muestra la lista de Pokemones capturados
    
    for i in lista_pokemones: #* Ciclo para mostrar una lista de los Pokemones capturados
        print(super().Detalles_Pokemon(i)) #* Muestra loss detalles de cada Pokemon capturado
        
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
            for i in lista_pokemones:
                if i.nombre == "Squirtle":    
                    super().Detalles_Pokemon(i) #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                for i in lista_pokemones:#* se actualiza si estado de atrapado a true
                    if i.nombre == "Squirtle":
                        i.atrapado = True
                print("\nHas elegido a Squirtle!\n")
                return lista_pokemones.add(lista_pokemones[0]) #* agrega el objeto Pokemon elegido(Squirtle) a tu lista de pokemones capturados
            else:
                continue
    
        elif opc == 2:
            for i in lista_pokemones:
                if i.nombre == "Charmander":    
                    super().Detalles_Pokemon(i) #* Muestra los detalles de un Pokemon
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                for i in lista_pokemones:#* se actualiza si estado de atrapado a true
                    if i.nombre == "Charmander":
                        i.atrapado = True
                print("\nHas elegido a Charmander!\n")
                return lista_pokemones.add(lista_pokemones_iniciales[1]) #* agrega el objeto Pokemon elegido(Charmander) a tu lista de pokemones capturados
            else:
                continue
        
        elif opc == 3:
            for i in lista_pokemones:
                if i.nombre == "Shinx":    
                    super().Detalles_Pokemon(i)
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                for i in lista_pokemones:#* se actualiza si estado de atrapado a true
                    if i.nombre == "Shinx":
                        i.atrapado = True
                print("\nHas elegido a Shinx!\n")
                return lista_pokemones.add(lista_pokemones[2]) #* agrega el objeto Pokemon elegido(Shinx) a tu lista de pokemones capturados
            else:
                continue
        
        elif opc == 4:
            for i in lista_pokemones:
                if i.nombre == "Bulbasaur":    
                    super().Detalles_Pokemon(i)
            eleccion = input("\nEstas seguro de tu eleccion? \n")
            if eleccion == "si":
                for i in lista_pokemones:#* se actualiza si estado de atrapado a true
                    if i.nombre == "Bulbasaur":
                        i.atrapado = True
                print("\nHas elegido a Bulbasaur!\n")
                return lista_pokemones.add(lista_pokemones[3]) #* agrega el objeto Pokemon elegido(Bulbasaur) a tu lista de pokemones capturados
            else:
                continue
        
        else:
            print("\nOpcion no valida!\n")
            continue
        

def Menu_Entrenar_Pokemon_Manual(): #? Muestra el menu para entrenar a un Pokemon
    
    Pokemones_Capturados() #* Muestra la lista de Pokemones capturados
    
    pokemon_en_entrenamiento = input("Que pokemon deseas entrenar?") #* Pregunta al usuario que Pokemon desea entrenar
    
    print("\n||--------Opciones para Pokemon---------||")
    print("|| 1 -> Entrenar Vida                   ||")
    print("|| 2 -> Entrenar Ataque                 ||")
    print("|| 3 -> Entrenar Defensa                ||")
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||\n")
    
    while True:
        
        opc = int(input("\nIngrese opcion: "))
        
        if opc == 1: #* Metodo para entrenar la vida de un Pokemon
            pokemon_en_entrenamiento.subir_vida() #* Metodo que aumenta los atributos del pokemon 
    
        elif opc == 2:  #* Metodo para entrenar el ataque de un Pokemon
            pokemon_en_entrenamiento.subir_ataque() #* Metodo que aumenta los atributos del pokemon
        
        elif opc == 3:  #* Metodo para entrenar la defensa de un Pokemon
            pokemon_en_entrenamiento.subir_defensa() #* Metodo que aumenta los atributos del pokemon
        
        else:
            print("\nOpcion no valida!\n")
            continue

def Menu_Actualizar_Pokemon(): #? Muestra el menu para actualizar los detalles de un Pokemon
    
    Pokemones_Capturados() #* Muestra la lista de Pokemones capturados
    print("\nno actualiza el nivel del pokemon, para eso debes entrenarlo!\n")
    
    pokemon_para_actualizar = input("Que pokemon deseas actualizar?") #* Pregunta al usuario que Pokemon desea entrenar
        
    for i in lista_pokemones:
        if i == pokemon_para_actualizar - 1:
            super().actualizar(i)

def Crear_Pokemon_Enemigo(): #? Crea un Pokemon enemigo aleatorio
    tipo = input("Que tipo de Pokemon deseas crear? (Agua, Fuego, Electro, Hierba): ")
    nombre = input("Nombre del Pokemon: ")
    vida = int(input("Vida del Pokemon(entre 100 - 500): "))
    ataque = int(input("Ataque del Pokemon(entre 10 - 100): "))
    defensa = int(input("Defensa del Pokemon(entre 10 - 100): "))
    ataque_especial = input("Ataque Especial del Pokemon: ")
    
    if tipo == "Agua":
        lista_pokemones_enemigos.add(Agua(nombre=nombre, vida=vida, ataque=ataque, defensa=defensa, ataque_agua=ataque_especial)) #* Creacion de un objeto de tipo Agua
    elif tipo == "Fuego":
        lista_pokemones_enemigos.add(Fuego(nombre=nombre, vida=vida, ataque=ataque, defensa=defensa, ataque_fuego=ataque_especial)) #* Creacion de un objeto de tipo Fuego
    elif tipo == "Electro":
        lista_pokemones_enemigos.add(Electro(nombre=nombre, vida=vida, ataque=ataque, defensa=defensa, ataque_electro=ataque_especial)) #* Creacion de un objeto de tipo Electro
    elif tipo == "Hierba":
        lista_pokemones_enemigos.add(Hierba(nombre=nombre, vida=vida, ataque=ataque, defensa=defensa, ataque_hierba=ataque_especial)) #* Creacion de un objeto de tipo Hierba

def Capturar_Pokemon(pokemom_para_capturar, vida_inicio_enemigo, vida_inicio_jugador): #? Captura un Pokemon enemigo
    
    if pokemom_para_capturar.vida > 0:
        print("\nNo puedes capturar a este Pokemon!\n")
    elif vida_inicio_enemigo < vida_inicio_jugador and pokemom_para_capturar.vida == 0:
        pokemom_para_capturar.atrapado = True
        lista_pokemones.add(pokemom_para_capturar)

def Batalla_Pokemon(): #? Simula una batalla entre dos Pokemones
    pass #TODO: falta crear este metodo




def Saludo_Inicial():#? Saluda al usuario por primera vez en el juego, mostrando el nombre del juego y una breve descripcion
    
    print("\n||------------------------------Examen-Pokemon------------------------------||\n")
    nombre = input("Ingrese su nombre: ")
    print(f"\nBienvenido al Juego {nombre}!")
    print("Este es un Juego de Pokemon, donde podras capturar, entrenar a tus propios Pokemon y tener \nbatallas con otros Pokemon salvajes!")
    print("\n||--------------------------------------------------------------------------||\n")

#! Codigo Principal

#? Saludo al usuario
Saludo_Inicial() #* Saluda al usuario por primera vez en el juego, mostrando el nombre del juego y una breve descripcion

#? Elegir Pokemos Inicial
Pokemon_Inicial = menu_elegir_pokemon() #* Muestra el menu para elegir el pokemon inicial

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

#cambio hecho para ver si ya todo funciona
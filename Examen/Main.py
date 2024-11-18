'''
#! Isai Almeraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Interaccion con el usuario(Main)
'''
#? Librerias
import random as rd
from Agua import Agua #* Libreria para generar numeros aleatorios
from Electro import Electro #* Libreria para generar numeros aleatorios
from Fuego import Fuego #* Libreria para generar numeros aleatorios
from Hierba import Hierba #* Libreria para generar numeros

#? Variales
lista_pokemones_iniciales = [] #* Lista para almacenar los Pokemones iniciales(Para elegir uno)
lista_pokemones_enemigos = [] #* Lista para almacenar los Pokemones enemigos
lista_pokemones = [] #* Lista para almacenar los Pokemones capturados

#? LLamadas a Clases

#! Creacion de Objetos
#? Creacion de Pokemones Principales
lista_pokemones_iniciales.append(Agua(nombre="Squirtel", desc=" Pokémon de tipo Agua con una excelente defensa y gran energía.", vida=100, ataque=10, defensa=10, ataque_agua="Hidrobomba")) #* Creacion de un objeto de tipo Agua
lista_pokemones_iniciales.append(Fuego(nombre="Charmander", desc="Pokémon de tipo Fuego ágil y lleno de determinación.", vida=100, ataque=10, defensa=10, ataque_fuego="Lanzallamas")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_iniciales.append(Electro(nombre="Shinx", desc=" Pokémon de tipo Electro pequeño pero lleno de energía eléctrica.", vida=100, ataque=10, defensa=10, ataque_electro="Rayo")) #* Creacion de un objeto de tipo Electro
lista_pokemones_iniciales.append(Hierba(nombre="Bulbasaur", desc=" Pokémon de tipo Hierba con un gran equilibrio entre fuerza y resistencia.", vida=100, ataque=10, defensa=10, ataque_hierba="Latigo Cepa")) #* Creacion de un objeto de tipo Hierba

#? Creacion de Pokemones Enemigos  
lista_pokemones_enemigos.append(Fuego(nombre="Vulpix", desc="Pokémon de tipo Fuego con un porte elegante y gran agilidad.", vida=250, ataque=40, defensa=30, ataque_fuego="Lanzallamas")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_enemigos.append(Agua(nombre="Golduck", desc="Pokémon de tipo Agua resistente y muy versátil en combate.", vida=350, ataque=30, defensa=30, ataque_agua="Hidrobomba")) #* Creacion de un objeto de tipo Agua
lista_pokemones_enemigos.append(Electro(nombre="Electrabuzz", desc="Pokémon de tipo Electro con una fuerza impresionante y energía constante.", vida=450, ataque=50, defensa=60, ataque_electro="Rayo")) #* Creacion de un objeto de tipo Electro
lista_pokemones_enemigos.append(Hierba(nombre="Gloom", desc=" Pokémon de tipo Hierba con un estilo peculiar y muy persistente", vida=150, ataque=20, defensa=25, ataque_hierba="Latigo Cepa")) #* Creacion de un objeto de tipo Hierba

#? Funciones

#? Metodo para mostrar los pokemones capturados
def Pokemones_Capturados():  #? Muestra la lista de Pokemones capturados
    if not lista_pokemones:  #* Verifica si no hay Pokémon capturados
        print("No has capturado ningún Pokémon aún.")
        return

    for idx, pokemon in enumerate(lista_pokemones, start=1):
        print(f"|| Pokémon #{idx} ||\n")
        pokemon.detalles_pokemon()  #* Llama al método detalles_pokemon
        
def menu_principal():  #? Muestra el menu principal del juego
    print("\n||--------Opciones para Pokemon---------||")
    print("|| 1 -> Crear Pokemon enemigos          ||")
    print("|| 2 -> Simular Batalla                 ||")
    print("|| 3 -> Mostrar Pokemon Capturados      ||")
    print("|| 4 -> Actualizar Detalles del Pokemon ||")
    print("|| 5 -> Entrenar Pokemon                ||")
    print("|| 9 -> Salir                           ||")
    print("||--------------------------------------||\n")

    while True:
        try:
            opcion = int(input("\nIngrese opcion: "))
            if opcion in [1, 2, 3, 4, 5, 9]:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

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
        try:
            opc = int((input("Elige tu Pokémon inicial:")))
            print("\n||----------------------------------------||\n")

            if opc == 1:
                for i in lista_pokemones_iniciales:
                    if i.nombre == "Squirtel":
                        i.detalles_pokemon()
                        break
                eleccion = input("\n¿Estas seguro de tu eleccion? (si/no): ").lower()
                if eleccion == "si":
                    for i in lista_pokemones_iniciales:
                        if i.nombre == "Squirtel":
                            i.atrapado = True
                            lista_pokemones.append(i)
                            print("\n¡Has elegido a Squirtel!\n")
                            return i
                else:
                    continue

            elif opc == 2:
                for i in lista_pokemones_iniciales:
                    if i.nombre == "Charmander":
                        i.detalles_pokemon()
                        break
                eleccion = input("\n¿Estas seguro de tu eleccion? (si/no): ").lower()
                if eleccion == "si":
                    for i in lista_pokemones_iniciales:
                        if i.nombre == "Charmander":
                            i.atrapado = True
                            lista_pokemones.append(i)
                            print("\n¡Has elegido a Charmander!\n")
                            return i
                else:
                    continue

            elif opc == 3:
                for i in lista_pokemones_iniciales:
                    if i.nombre == "Shinx":
                        i.detalles_pokemon()
                        break
                eleccion = input("\n¿Estas seguro de tu eleccion? (si/no): ").lower()
                if eleccion == "si":
                    for i in lista_pokemones_iniciales:
                        if i.nombre == "Shinx":
                            i.atrapado = True
                            lista_pokemones.append(i)
                            print("\n¡Has elegido a Shinx!\n")
                            return i
                else:
                    continue

            elif opc == 4:
                for i in lista_pokemones_iniciales:
                    if i.nombre == "Bulbasaur":
                        i.detalles_pokemon()
                        break
                eleccion = input("\n¿Estas seguro de tu eleccion? (si/no): ").lower()
                if eleccion == "si":
                    for i in lista_pokemones_iniciales:
                        if i.nombre == "Bulbasaur":
                            i.atrapado = True
                            lista_pokemones.append(i)
                            print("\n¡Has elegido a Bulbasaur!\n")
                            return i
                else:
                    continue

            else:
                print("\nOpcion no valida. Por favor, ingresa un número entre 1 y 4.\n")
                continue

        except ValueError:
            print("\nEntrada inválida. Por favor, ingresa un número.\n")

def Menu_Entrenar_Pokemon_Manual():
    Pokemones_Capturados()  # Muestra la lista de Pokemones capturados

    try:
        pokemon_idx = int(input("¿Qué Pokémon deseas entrenar? (Ingresa el número): ")) - 1
        if 0 <= pokemon_idx < len(lista_pokemones):
            pokemon_en_entrenamiento = lista_pokemones[pokemon_idx]

            print("\n||--------Opciones para Entrenamiento---------||")
            print("|| 1 -> Entrenar Vida                         ||")
            print("|| 2 -> Entrenar Ataque                       ||")
            print("|| 3 -> Entrenar Defensa                      ||")
            print("|| 9 -> Salir                                 ||")
            print("||--------------------------------------------||\n")

            while True:
                try:
                    opc = int(input("\nIngrese opción: "))
                    if opc == 1:
                        pokemon_en_entrenamiento.subirVida()
                        print(f"La vida de {pokemon_en_entrenamiento.nombre} ha aumentado.")
                    elif opc == 2:
                        pokemon_en_entrenamiento.subirAtaque()
                        print(f"El ataque de {pokemon_en_entrenamiento.nombre} ha aumentado.")
                    elif opc == 3:
                        pokemon_en_entrenamiento.subirDefensa()
                        print(f"La defensa de {pokemon_en_entrenamiento.nombre} ha aumentado.")
                    elif opc == 9:
                        print("Saliendo del entrenamiento.")
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Ingresa un número.")
        else:
            print("Índice fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")

def Menu_Actualizar_Pokemon():  # Muestra el menú para actualizar los detalles de un Pokémon
    Pokemones_Capturados()  # Muestra la lista de Pokemones capturados
    print("\nNo actualiza el nivel del Pokémon, para eso debes entrenarlo!\n")

    try:
        pokemon_idx = int(input("¿Qué Pokémon deseas actualizar? (Ingresa el número): ")) - 1
        if 0 <= pokemon_idx < len(lista_pokemones):
            pokemon = lista_pokemones[pokemon_idx]
            pokemon.actualizar()  # Llama al método actualizar del objeto Pokémon
        else:
            print("Índice fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")

def Crear_Pokemon_Enemigo(): #? Crea un Pokemon enemigo aleatorio
    tipo = input("Que tipo de Pokemon deseas crear? (Agua, Fuego, Electro, Hierba): ")
    nombre = input("Nombre del Pokemon: ")
    descripcion = input("Descripcion del Pokemon: ")
    vida = int(input("Vida del Pokemon(entre 100 - 500): "))
    ataque = int(input("Ataque del Pokemon(entre 10 - 100): "))
    defensa = int(input("Defensa del Pokemon(entre 10 - 100): "))
    ataque_especial = input("Ataque Especial del Pokemon: ")
    
    if tipo == "Agua":
        lista_pokemones_enemigos.append(Agua(nombre=nombre, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_agua=ataque_especial)) #* Creacion de un objeto de tipo Agua
    elif tipo == "Fuego":
        lista_pokemones_enemigos.append(Fuego(nombre=nombre, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_fuego=ataque_especial)) #* Creacion de un objeto de tipo Fuego
    elif tipo == "Electro":
        lista_pokemones_enemigos.append(Electro(nombre=nombre, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_electro=ataque_especial)) #* Creacion de un objeto de tipo Electro
    elif tipo == "Hierba":
        lista_pokemones_enemigos.append(Hierba(nombre=nombre, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_hierba=ataque_especial)) #* Creacion de un objeto de tipo Hierba

def Capturar_Pokemon(pokemon_para_capturar, vida_inicio_enemigo, vida_inicio_jugador):  #? Captura un Pokemon enemigo
    
    #? Verifica si el Pokémon enemigo puede ser capturado
    if pokemon_para_capturar.vida > 0:  #* El Pokémon aún tiene vida
        print("\nNo puedes capturar a este Pokémon. Aún tiene vida!\n")
        return

    if vida_inicio_enemigo < vida_inicio_jugador:  #* Vida inicial del enemigo es menor
        pokemon_para_capturar.atrapado = True  #* Cambia el estado a capturado
        lista_pokemones.append(pokemon_para_capturar)  #* Agrega a la lista del jugador
        lista_pokemones_enemigos.remove(pokemon_para_capturar)  #* Elimina el Pokémon de la lista de enemigos
        print(f"\n¡Felicidades! Has capturado a {pokemon_para_capturar.nombre}!\n")
    else:
        print("\nNo puedes capturar al Pokémon. Su nivel de vida inicial era mayor o igual al tuyo.\n")

def Batalla_Pokemon(): #? Simula una batalla entre dos Pokemones
    
    #? Mensaje para jugador
    print("\n||------------------Batalla------------------||")
    print("\nHaz entrado a un combate!\n")
    
    #? Muestra el pokemon enemigo con el que se va a pelear
    print("\n||------------------Pokemon Enemigo------------------||\n")
    pokemon_enemigo_combate = rd.choice(lista_pokemones_enemigos)  #* Selecciona un Pokémon enemigo aleatorio
    pokemon_enemigo_combate.detalles_pokemon()  #* Llama al método para mostrar detalles del Pokémon enemigo
    print("\n||---------------------------------------------------||\n")
    
    #? Muestra los Pokemones capturados para elegir uno para la batalla
    print("\n||------------------Tus Pokemones------------------||\n")
    Pokemones_Capturados() #* Muestra la lista de Pokemones capturados
    
    try:    #* Muetsra un mensaje de error si la seleccion no es valida
        eleccion = int(input("\nSelecciona tu Pokémon para la batalla: ")) - 1
        pokemon_jugador_combate = lista_pokemones[eleccion]  #* Selecciona el Pokémon del jugador
    except (ValueError, IndexError):
        print("Selección inválida. Por favor, inténtalo de nuevo.")
        return
    
    #? Capturo la vida inicial de los Pokemones
    vida_pokemon_jugador = pokemon_jugador_combate.vida #* Captura la vida inicial del Pokemon jugador para comparar al final antes de capturar
    vida_pokemon_enemigo = pokemon_enemigo_combate.vida #* Captura la vida inicial del Pokemon enemigo para comparar al final antes de capturar
    
    #? Ciclo para la batalla
    turno = 1 #* Variable para llevar el control de los turnos | 1 = Jugador | 2 = Enemigo
    
    #? boolean para saber si alun pokemn activo su defensa  
    defensa_activa_jugador = False
    defensa_activa_enemigo = False
    
    #? boolean para ver si ej jugador gano la batalla
    gano = False
    
    #? se inicializa el ciclo de la batalla
    while vida_pokemon_jugador > 0 and vida_pokemon_enemigo > 0: #* Ciclo para la batalla
        if turno == 1:
            print("\n||------------------Turno Jugador------------------||")
            print("|| 1 -> Atacar                                     ||")
            print("|| 2 -> Defensa                                    ||")
            print("||-------------------------------------------------||\n")
            opc = int(input("Que deseas hacer? "))
            
            if opc == 1:
                print("||------------------Ataque------------------||\n")
                if defensa_activa_enemigo:  #* si el enemigo activo su defensa, solo se le resta un 75% del ataque
                    pokemon_enemigo_combate.vida -= pokemon_jugador_combate.ataque * 0.75
                    print(f"El Pokemon enemigo ha recibido {pokemon_jugador_combate.ataque * 0.75} de daño")
                    print(f"Vida del Pokemon enemigo: {pokemon_enemigo_combate.vida}\n")
                    turno = 2
                else:
                    pokemon_enemigo_combate.vida -= pokemon_jugador_combate.ataque
                    print(f"El Pokemon enemigo ha recibido {pokemon_jugador_combate.ataque} de daño")
                    print(f"Vida del Pokemon enemigo: {pokemon_enemigo_combate.vida}\n")
                    turno = 2
            elif opc == 2:
                print("||------------------Defensa------------------||\n")
                defensa_activa_jugador = True
                print("Defensa activada!")
                turno = 2
                
        elif turno == 2:
            print("||------------------Turno Enemigo------------------||\n")
            opc = rd.randint(1, 2)
            
            if opc == 1:
                print("||------------------Ataque------------------||\n")
                print("El pokemon enemigo ataca!")
                if defensa_activa_jugador:
                    pokemon_jugador_combate.vida -= pokemon_enemigo_combate.ataque * 0.75
                    print(f"Tu Pokemon ha recibido {pokemon_enemigo_combate.ataque * 0.75} de daño")
                    print(f"Vida de tu Pokemon: {pokemon_jugador_combate.vida}\n")
                    turno = 1
                else:
                    pokemon_jugador_combate.vida -= pokemon_enemigo_combate.ataque
                    print(f"Tu Pokemon ha recibido {pokemon_enemigo_combate.ataque} de daño")
                    print(f"Vida de tu Pokemon: {pokemon_jugador_combate.vida}\n")
                    turno = 1
            elif opc == 2:
                print("||------------------Defensa------------------||\n")
                defensa_activa_enemigo = True
                print("Defensa de pokemon enemigo activada!")
                turno = 1
    
        if pokemon_jugador_combate.vida <= 0:
            print("\nHas perdido la batalla!\n")
            break
        elif pokemon_enemigo_combate.vida <= 0:
            print("\n¡Has ganado la batalla!\n")
            gano = True
            break
        
    if gano:
        print("||------------------Capturar Pokémon------------------||\n")
        eleccion = input("¿Deseas capturar al Pokémon enemigo? (si/no): ").lower()
        if eleccion == "si":
            Capturar_Pokemon(pokemon_enemigo_combate, vida_pokemon_enemigo, vida_pokemon_jugador)  #* Llama a la función de captura
        else:
            print("\nNo has capturado al Pokémon enemigo.\n")
    
    print("Fin del combate!\n")
    print("||---------------------------------------------------||\n")

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
    try:
        opc = menu_principal()  #* Muestra el menú principal del juego 

        if opc == 9:  #* Salir
            # Mandar mensaje resumiendo cuántos Pokémon capturó, cuántas derrotas tuvo y cuántas victorias
            print("\nSaliendo...\nGracias por usar el programa!")
            break  #* Termina el programa al elegir la opción de salida en el menú principal

        elif opc == 1:  #* Método para crear un nuevo Pokémon enemigo
            Crear_Pokemon_Enemigo()  #* Llama a la función para crear un Pokémon enemigo
        
        elif opc == 2:  #* Método para simular una batalla entre dos Pokemones
            if not lista_pokemones:  # Verifica si el usuario tiene Pokémon capturados
                print("\nNo tienes Pokémon capturados. No puedes entrar a una batalla.\n")
            elif not lista_pokemones_enemigos:  # Verifica si hay Pokémon enemigos
                print("\nNo hay Pokémon enemigos disponibles. Por favor, crea uno primero.\n")
            else:
                Batalla_Pokemon()  #* Llama a la función para realizar una batalla
        
        elif opc == 3:  #* Mostrar Lista de Pokemones Capturados y sus detalles
            Pokemones_Capturados()  #* Muestra los Pokémon capturados y sus detalles
        
        elif opc == 4:  #* Método para Actualizar los niveles de ataque, defensa y vida Pokémon individualmente
            if not lista_pokemones:  # Verifica si el usuario tiene Pokémon capturados
                print("\nNo tienes Pokémon capturados para actualizar.\n")
            else:
                Menu_Actualizar_Pokemon()  #* Llama al menú para actualizar los detalles de un Pokémon
                
        elif opc == 5:  #* Método para Entrenar los niveles de ataque, defensa y vida Pokémon
            if not lista_pokemones:  # Verifica si el usuario tiene Pokémon capturados
                print("\nNo tienes Pokémon capturados para entrenar.\n")
            else:
                Menu_Entrenar_Pokemon_Manual()  #* Llama al menú para entrenar un Pokémon manualmente
        
        
        else:
            print("\nOpción no válida!\n")

    except ValueError:
        print("\nEntrada inválida. Por favor, ingresa un número válido.\n")


print("\n||--------------------------------------------------------------------------||\n")
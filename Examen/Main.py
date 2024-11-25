#? Librerias
import random as rd
from Skills import Agua, Fuego, Electro, Hierba #* Importar las clases de los pokemones

#? Variales
lista_pokemones_iniciales = [] #* Lista para almacenar los Pokemones iniciales(Para elegir uno)
lista_pokemones_enemigos = [] #* Lista para almacenar los Pokemones enemigos
lista_pokemones = [] #* Lista para almacenar los Pokemones capturados

#? LLamadas a Clases

#! Creacion de Objetos
#? Creacion de Pokemones Principales
lista_pokemones_iniciales.append(Agua(nombre="Psyduck",nombreEv2="Golduck",nombreEv3="Golduck", desc="Dios mismo", vida=100, ataque=999, defensa=999, ataque_agua="waterGun", level="20")) #* Creacion de un objeto de tipo Agua
lista_pokemones_iniciales.append(Fuego(nombre="Charmander",nombreEv2="Charmeleon",nombreEv3="Charizard", desc="Pokémon de tipo Fuego ágil y lleno de determinación.", vida=100, ataque=10, defensa=10, ataque_fuego="Lanzallamas", level="32")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_iniciales.append(Electro(nombre="Shinx",nombreEv2="Luxio",nombreEv3="Luxray", desc=" Pokémon de tipo Electro pequeño pero lleno de energía eléctrica.", vida=100, ataque=10, defensa=10, ataque_electro="Rayo", level="15")) #* Creacion de un objeto de tipo Electro
lista_pokemones_iniciales.append(Hierba(nombre="Bulbasaur",nombreEv2="Ivysaur",nombreEv3="Venusaur", desc=" Pokémon de tipo Hierba con un gran equilibrio entre fuerza y resistencia.", vida=100, ataque=10, defensa=10, ataque_hierba="Latigo Cepa", level="15")) #* Creacion de un objeto de tipo Hierba

#? Creacion de Pokemones Enemigos  
lista_pokemones_enemigos.append(Fuego(nombre="Vulpix",nombreEv2="Ninetales",nombreEv3="Ninetales", desc="Pokémon de tipo Fuego con un porte elegante y gran agilidad.", vida=250, ataque=40, defensa=30, ataque_fuego="Lanzallamas", level="46")) #* Creacion de un objeto de tipo Fuego
lista_pokemones_enemigos.append(Agua(nombre="Golduck",nombreEv2="Golduck",nombreEv3="Golduck", desc="Pokémon de tipo Agua resistente y muy versátil en combate.", vida=350, ataque=30, defensa=30, ataque_agua="Hidrobomba", level="85")) #* Creacion de un objeto de tipo Agua
lista_pokemones_enemigos.append(Electro(nombre="Electrabuzz",nombreEv2="Electrabuzz",nombreEv3="Electivire", desc="Pokémon de tipo Electro con una fuerza impresionante y energía constante.", vida=450, ataque=50, defensa=60, ataque_electro="Rayo", level="99")) #* Creacion de un objeto de tipo Electro
lista_pokemones_enemigos.append(Hierba(nombre="Gloom",nombreEv2="Gloom",nombreEv3="Bellossom", desc=" Pokémon de tipo Hierba con un estilo peculiar y muy persistente", vida=150, ataque=20, defensa=25, ataque_hierba="Latigo Cepa", level="34")) #* Creacion de un objeto de tipo Hierba

#? Funciones, level="N/A"

#? Metodo para mostrar los pokemones capturados
def Pokemones_Capturados():  #? Muestra la lista de Pokemones capturados
    
    if not lista_pokemones:  #* Verifica si no hay Pokémon capturados
        print("No has capturado ningún Pokémon aún.")
        return

    for idx, pokemon in enumerate(lista_pokemones, start=1):
        print(f"|| Pokémon #{idx} ||\n")
        pokemon.detalles_pokemon()  #* Llama al método detalles_pokemon
        
def menu_principal():  #? Muestra el menu principal del juego
    
    while True:
        print("\n||--------Opciones para Pokemon---------||")
        print("|| 1 -> Crear Pokemon enemigos          ||")
        print("|| 2 -> Simular Batalla                 ||")
        print("|| 3 -> Mostrar Pokemon Capturados      ||")
        print("|| 4 -> Actualizar Detalles del Pokemon ||")
        print("|| 5 -> Entrenar Pokemon                ||")
        print("|| 9 -> Salir                           ||")
        print("||--------------------------------------||\n")

        try:
            opcion = int(input("\nIngrese opcion: "))
            if opcion in [1, 2, 3, 4, 5, 9]:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def menu_elegir_pokemon():  #? Muestra el menu para elegir el pokemon inicial
    
    pokemon_elegido = False
    
    while not pokemon_elegido:
        print("\n||------------------Menu------------------||")
        print("||        Aun no tienes un Pokemon        ||")
        print("||    Elige a tu pokemon para iniciar!    ||")
        print("||****************************************||")
        print("|| 1 -> Spyduck(Agua)                     ||")
        print("|| 2 -> Charmander(Fuego)                 ||")
        print("|| 3 -> Shinx(Electrico)                  ||")
        print("|| 4 -> Bulbasaur(Hierba)                 ||")
        print("||----------------------------------------||\n")

        try:
            opc = int((input("Elige tu Pokémon inicial:")))
            print("\n||----------------------------------------||\n")

            if opc == 1:
                for i in lista_pokemones_iniciales:
                    if i.nombre == "Psyduck":
                        i.detalles_pokemon()
                        break
                eleccion = input("\n¿Estas seguro de tu eleccion? (si/no): ").lower()
                if eleccion == "si":
                    for i in lista_pokemones_iniciales:
                        if i.nombre == "Psyduck":
                            i.atrapado = True
                            lista_pokemones.append(i)
                            print("\n¡Has elegido a Psyduck!\n")
                            pokemon_elegido = True
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
                            pokemon_elegido = True
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
                            pokemon_elegido = True
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
                            pokemon_elegido = True
                else:
                    continue

            else:
                print("\nOpcion no valida. Por favor, ingresa un número entre 1 y 4.\n")
                continue

        except ValueError:
            print("\nEntrada inválida. Por favor, ingresa un número.\n")

def Menu_Entrenar_Pokemon_Manual():
    Pokemones_Capturados()  #* Muestra la lista de Pokemones capturados

    try:
        pokemon_idx = int(input("¿Qué Pokémon deseas entrenar? (Ingresa el número): ")) - 1
        if 0 <= pokemon_idx < len(lista_pokemones):
            pokemon_en_entrenamiento = lista_pokemones[pokemon_idx]

            while True:
                
                print("\n||--------Opciones para Entrenamiento---------||")
                print("|| 1 -> Entrenar Vida                         ||")
                print("|| 2 -> Entrenar Ataque                       ||")
                print("|| 3 -> Entrenar Defensa                      ||")
                print("|| 4 -> Subir Nivel                           ||")
                print("|| 9 -> Salir                                 ||")
                print("||--------------------------------------------||\n")

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
                    elif opc == 4:
                        pokemon_en_entrenamiento.subirNivel()
                        if pokemon_en_entrenamiento.evol != 3:
                            print(f"El nivel de {pokemon_en_entrenamiento.nombre} ha aumentado.")
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
    
    print("\n||--------------tipo de pokemon---------------||")
    print("|| 1 -> Agua                                  ||")
    print("|| 2 -> Fuego                                 ||")
    print("|| 3 -> Electro                               ||")
    print("|| 4 -> Hierba                                ||")
    print("||--------------------------------------------||\n")
    
    tipo = int(input("Que tipo de Pokemon deseas crear? "))
    nombre = input("Nombre del Pokemon Evolucion 1: ")
    nombreEv2 = input("Nombre del Pokemon Evolucion 2: ")
    nombreEv3 = input("Nombre del Pokemon Evolucion 3: ")
    descripcion = "Un Pokemon salvaje que te ha retado a una batalla."
    vida = rd.randint(100, 500)
    ataque = rd.randint(10, 100)
    defensa = rd.randint(10, 100)
    ataque_especial = input("ataque especial: ")
    
    if tipo == 1:
        lista_pokemones_enemigos.append(Agua(nombre=nombre, nombreEv2 = nombreEv2, nombreEv3 = nombreEv3, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_agua=ataque_especial)) #* Creacion de un objeto de tipo Agua
    elif tipo == 2:
        lista_pokemones_enemigos.append(Fuego(nombre=nombre, nombreEv2 = nombreEv2, nombreEv3 = nombreEv3, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_fuego=ataque_especial)) #* Creacion de un objeto de tipo Fuego
    elif tipo == 3:
        lista_pokemones_enemigos.append(Electro(nombre=nombre, nombreEv2 = nombreEv2, nombreEv3 = nombreEv3, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_electro=ataque_especial)) #* Creacion de un objeto de tipo Electro
    elif tipo == 4:
        lista_pokemones_enemigos.append(Hierba(nombre=nombre, nombreEv2 = nombreEv2, nombreEv3 = nombreEv3, desc = descripcion, vida=vida, ataque=ataque, defensa=defensa, ataque_hierba=ataque_especial)) #* Creacion de un objeto de tipo Hierba
    else:
        print("Tipo de pokemon no válido. Por favor, inténtalo de nuevo.")
        
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

def Batalla_Pokemon():
    
    #* Define colores
    RESET = "\033[0m"   #* Reinicia color
    ROJO = "\033[91m"   #* Rojo brillante (enemigo)
    VERDE = "\033[92m"  #* Verde brillante (jugador)
    AZUL = "\033[94m"   #* Azul brillante (mensajes neutros)
    
    print(f"{AZUL}||-------------------------------------------------||")
    print("             ¡ENTRASTE EN UNA BATALLA!")
    print(f"||-------------------------------------------------||{RESET}")

    print(f"{ROJO}||-------------------------------------------------||")
    print("               POKÉMON ENEMIGO APARECE")
    print(f"||-------------------------------------------------||{RESET}")
    
    pokemon_enemigo_combate = rd.choice(lista_pokemones_enemigos)
    pokemon_enemigo_combate.detalles_pokemon()

    print(f"{VERDE}||-------------------------------------------------||")
    print("                    TUS POKÉMONS")
    print(f"||-------------------------------------------------||{RESET}")
    Pokemones_Capturados()

    try:
        eleccion = int(input(f"\n{VERDE}Selecciona tu Pokémon para la batalla: {RESET}")) - 1
        pokemon_jugador_combate = lista_pokemones[eleccion]
    except (ValueError, IndexError):
        print(f"{ROJO}⚠️ Selección inválida. Por favor, inténtalo de nuevo.{RESET}")
        return

    vida_pokemon_jugador = pokemon_jugador_combate.vida
    vida_pokemon_enemigo = pokemon_enemigo_combate.vida

    turno = 1
    defensa_activa_jugador = defensa_activa_enemigo = False
    defensa_jugador = pokemon_jugador_combate.defensa
    defensa_enemigo = pokemon_enemigo_combate.defensa
    gano = False

    while vida_pokemon_jugador > 0 and vida_pokemon_enemigo > 0:
        if turno == 1:
            print(f"\n{VERDE}||------------------Turno Jugador------------------||{RESET}")
            print(f"{VERDE}|| 1 -> Atacar                                     ||{RESET}")
            print(f"{VERDE}|| 2 -> Defensa                                    ||{RESET}")
            print(f"{VERDE}||-------------------------------------------------||{RESET}\n")
            opc = int(input(f"{VERDE}¿Qué deseas hacer? {RESET}"))

            if opc == 1:
                print(f"{VERDE}||-------------------------------------------------||")
                print("                       ¡ATAQUE!")
                print(f"||-------------------------------------------------||{RESET}")
                damage = pokemon_jugador_combate.ataque * (0.75 if defensa_activa_enemigo else 1)
                
                if defensa_enemigo > 0:
                    if damage <= defensa_enemigo:
                        defensa_enemigo -= damage
                        print(f"\n{AZUL}✨ La defensa del enemigo absorbió {damage:.2f} de daño{RESET}")
                        damage = 0
                    else:
                        print(f"\n{AZUL}✨ La defensa del enemigo se destruyó ({defensa_enemigo:.2f} absorbido){RESET}")
                        damage -= defensa_enemigo
                        defensa_enemigo = 0
                if damage > 0:
                    vida_pokemon_enemigo = max(0, vida_pokemon_enemigo - damage)
                    print(f"{AZUL}⚔️  Daño a la vida del enemigo: {damage:.2f}{RESET}")
                print(f"{AZUL}❤️  Vida del enemigo: {vida_pokemon_enemigo}  |  🛡️  Defensa: {defensa_enemigo}{RESET}")
                turno = 2

            elif opc == 2:
                print(f"{VERDE}||-------------------------------------------------||")
                print("                  ¡DEFENSA ACTIVADA!")
                print(f"||-------------------------------------------------||{RESET}")
                defensa_activa_jugador = True
                turno = 2

        elif turno == 2:
            print(f"\n{ROJO}||------------------Turno Enemigo------------------||{RESET}")
            opc = rd.randint(1, 2)

            if opc == 1:
                print(f"{ROJO}||-------------------------------------------------||")
                print("                   ¡ATAQUE ENEMIGO!")
                print(f"||-------------------------------------------------||{RESET}")
                damage = pokemon_enemigo_combate.ataque * (0.75 if defensa_activa_jugador else 1)
                if defensa_jugador > 0:
                    if damage <= defensa_jugador:
                        defensa_jugador -= damage
                        print(f"\n{AZUL}✨ Tu defensa absorbió {damage:.2f} de daño{RESET}")
                        damage = 0
                    else:
                        print(f"\n{AZUL}✨ Tu defensa se destruyó ({defensa_jugador:.2f} absorbido){RESET}")
                        damage -= defensa_jugador
                        defensa_jugador = 0
                if damage > 0:
                    vida_pokemon_jugador = max(0, vida_pokemon_jugador - damage)
                    print(f"{AZUL}⚔️  Daño a tu vida: {damage:.2f}{RESET}")
                print(f"{AZUL}❤️  Tu Vida: {vida_pokemon_jugador}  |  🛡️  Tu Defensa: {defensa_jugador}{RESET}")
                turno = 1

            elif opc == 2:
                print(f"{ROJO}||-------------------------------------------------||")
                print("               ¡ENEMIGO ACTIVÓ DEFENSA!")
                print(f"||-------------------------------------------------||{RESET}")
                defensa_activa_enemigo = True
                turno = 1

    if vida_pokemon_jugador <= 0:
        print(f"\n{ROJO}❌ Has perdido la batalla...{RESET}\n")
    elif vida_pokemon_enemigo <= 0:
        print(f"\n{VERDE}✅ ¡Ganaste la batalla!{RESET}\n")
        gano = True

    if gano:
        print(f"{AZUL}||-------------------------------------------------||")
        print("                OPORTUNIDAD DE CAPTURA")
        print(f"||-------------------------------------------------||{RESET}")
        eleccion = input(f"{AZUL}¿Deseas capturar al Pokémon enemigo? (si/no): {RESET}").lower()
        if eleccion == "si":
            Capturar_Pokemon(pokemon_enemigo_combate, vida_pokemon_enemigo, vida_pokemon_jugador)
        else:
            print(f"\n{AZUL}No has capturado al Pokémon enemigo.{RESET}\n")

    print(f"{AZUL}||-------------------------------------------------||")
    print("                   FIN DEL COMBATE")
    print(f"||-------------------------------------------------||{RESET}")



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
            print("\nSaliendo...\nGracias por jugar pokedex!")
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


#TODO: Faltantes / Observaciones

#? NO debe dejar que salgan numros negativos en batalla

#? Menu debe aparecer despues de cada accion

#? A crear pokemon enemigo la creacion debe ser por menu

#? Implementar la evolucion de pokeomones

#? en batalla cuando usas la defensa, el ataque debe quitar puntos de la defensa y si se acaba la defensa, le quita la restante del ataque a la vida

#? pokemon debe hablar cuando se muestran detalles

#? crear un registro de batallas ganadas y perdidas, de quien ataco, quien defendio, si se capturo, etc
    #* extra, que cuadno se guarde  el registro que guarde los datos por num(batalla 1...) y que guarde el dia y la hora.
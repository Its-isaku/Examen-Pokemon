def Capturar_Pokemon(pokemon_para_capturar, vida_inicio_enemigo, vida_inicio_jugador):  #? Captura un Pokemon enemigo
    
    #? Verifica si el Pokémon enemigo puede ser capturado
    if pokemon_para_capturar.vida > 0:  #* El Pokémon aún tiene vida
        print("\nNo puedes capturar a este Pokémon. Aún tiene vida!\n")
        print(f"Vida actual del enemigo: {pokemon_para_capturar.vida}")

        return

    if vida_inicio_enemigo < vida_inicio_jugador:  #* Vida inicial del enemigo es menor
        pokemon_para_capturar.atrapado = True  #* Cambia el estado a capturado
        pokemon_para_capturar.vida = vida_inicio_enemigo  #* Restaura la vida del Pokémon a su valor inicial
        lista_pokemones.append(pokemon_para_capturar)  #* Agrega a la lista del jugador
        lista_pokemones_enemigos.remove(pokemon_para_capturar)  #* Elimina el Pokémon de la lista de enemigos
        print(f"\n¡Felicidades! Has capturado a {pokemon_para_capturar.nombre}!\n")
    else:
        print("\nNo puedes capturar al Pokémon. Su nivel de vida inicial era mayor o igual al tuyo.\n")
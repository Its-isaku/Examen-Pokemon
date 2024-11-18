'''
#! Sofia Almaraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase Fuego
'''
#? Librerias
from Pokemon import Pokemon   #* Importar la clase Base de PokemonBase

#? Clase Fuego
class Fuego(Pokemon):  #* Clase de pokémon de tipo fuego
    def __init__(self, ataque_fuego, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_fuego = ataque_fuego #* nombre del ataque especial de tipo fuego
    
    def hablar(self):   #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡pssssst!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y vida
        self.defensa += 13
        self.vida += 5
        print("Update:\n+13 Defensa XP\n+5 Vida XP")
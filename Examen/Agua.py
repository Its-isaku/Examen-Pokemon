'''
#! Sofia Almaraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase Agua
'''
#? Librerias
from PokemonBase import Base    #* Importar la clase Base de PokemonBase

#? Clase Agua
class Agua(Base):   #* Clase de pokémon de tipo agua
    def __init__(self, ataque_agua, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_agua = ataque_agua #* nombre del ataque especial de tipo agua
    
    def hablar(self):   #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡Gluglugluglu!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y vida
        self.defensa += 15
        self.vida += 5
        print("Update:\n+15 Defensa XP\n+5 Vida XP")
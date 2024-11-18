'''
#! Sofia Almaraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase Hierba
'''
#? Librerias
from PokemonBase import Base    #* Importar la clase Base de PokemonBase

#? Clase Hierba
class Hierba(Base):  #* Clase de pokémon de tipo hierba
    def __init__(self, ataque_hierba, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_hierba = ataque_hierba #* nombre del ataque especial de tipo hierba
    
    def hablar(self):   #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡aghhhhh!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y vida
        self.defensa += 9
        self.vida += 5
        print("Update:\n+9 Defensa XP\n+5 Vida XP")
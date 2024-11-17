from PokemonBase import base

class Electro(base):
    def __init__(self, ataque_electro, **kwargs):
        super().__init__(**kwargs) # uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_electro = ataque_electro # nombre del ataque especial de tipo electro
    
    def hablar(self):
        print(f"El Pokémon {self.nombre} dice: ¡brrrrrr!")
    
    def update(self):
        self.defensa += 11
        self.vida += 6
        print("Update:\n+11 Defensa XP\n+6 Vida XP")
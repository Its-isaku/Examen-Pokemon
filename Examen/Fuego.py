from PokemonBase import base

class Fuego(base):
    def __init__(self, ataque_fuego, **kwargs):
        super().__init__(**kwargs) # uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_fuego = ataque_fuego # nombre del ataque especial de tipo fuego
    
    def hablar(self):
        print(f"El Pokémon {self.nombre} dice: ¡pssssst!")
    
    def update(self):
        self.defensa += 13
        self.vida += 5
        print("Update:\n+13 Defensa XP\n+5 Vida XP")
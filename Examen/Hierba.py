from PokemonBase import base

class Hierba(base):
    def __init__(self, ataque_hierba, **kwargs):
        super().__init__(**kwargs) # uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_hierba = ataque_hierba # nombre del ataque especial de tipo hierba
    
    def hablar(self):
        print(f"El Pokémon {self.nombre} dice: ¡aghhhhh!")
    
    def update(self):
        self.defensa += 9
        self.vida += 5
        print("Update:\n+9 Defensa XP\n+5 Vida XP")
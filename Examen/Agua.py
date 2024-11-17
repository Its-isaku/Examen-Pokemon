from PokemonBase import base

class Agua(base):
    def __init__(self, ataque_agua, **kwargs):
        super().__init__(**kwargs) # uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_agua = ataque_agua # nombre del ataque especial de tipo agua
    
    def hablar(self):
        print(f"El Pokémon {self.nombre} dice: ¡Gluglugluglu!")
    
    def update(self):
        self.defensa += 15
        self.vida += 5
        print("Update:\n+15 Defensa XP\n+5 Vida XP")

'''pokemon = Agua(
    nombre = "Psyduck",
    desc = "Pato amarillo de tipo agua",
    ataque = 52,
    defensa = 48,
    vida = 50, # HP 
    level = 13,
    ataque_agua = "Water gun"
)

pokemon.hablar()
pokemon.update()'''
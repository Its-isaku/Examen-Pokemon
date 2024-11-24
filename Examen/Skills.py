#? Librerias
from Pokemon import Pokemon   #* Importar la clase Base de PokemonBase

#? Clase Agua
class Agua(Pokemon):   #* Clase de pokémon de tipo agua
    def __init__(self, ataque_agua, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_agua = ataque_agua #* nombre del ataque especial de tipo agua
    
    def hablar(self):   #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡Gluglugluglu!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y vida
        self.defensa += 15
        self.vida += 5
        print("Update:\n+15 Defensa XP\n+5 Vida XP")
    
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
        
#? Clase Hierba
class Hierba(Pokemon):  #* Clase de pokémon de tipo hierba
    def __init__(self, ataque_hierba, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_hierba = ataque_hierba #* nombre del ataque especial de tipo hierba
    
    def hablar(self):   #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡aghhhhh!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y vida
        self.defensa += 9
        self.vida += 5
        print("Update:\n+9 Defensa XP\n+5 Vida XP")
        
#? Clase Electro
class Electro(Pokemon): #* Clase de pokémon de tipo electrico
    def __init__(self, ataque_electro, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_electro = ataque_electro #* nombre del ataque especial de tipo electro
    
    def hablar(self): #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡brrrrrr!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y viday
        self.defensa += 11
        self.vida += 6
        print("Update:\n+11 Defensa XP\n+6 Vida XP")
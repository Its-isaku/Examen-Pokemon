from abc import ABC, abstractmethod

class base(ABC):
    def __init__(self, nombre="N/A", desc="N/A", ataque=0, defensa=0, vida=0, level=1, evol=1, atrapado=False):
        self.nombre = nombre
        self.desc = desc
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.level = level
        self.evol = evol
        self.atrapado = atrapado

    def hablar(self):
        pass

    def update(self):
        pass
    
    def update_lvl(self):
        self.level += 1
        while self.level >= 100: 
            self.level = 1 # cuando llega al nivel 100 o mas, regresar al nivel 1
            self.evol += 1 # aumentar evol dependiendo 

            # indicar en que nivel de evol va
            if self.evol == 1:
                print("Pokemon bebé")
            elif self.evol == 2:
                print("¡Tu Pokémon ha evolucionado!")
            elif self.evol >= 3:
                print("¡Tu Pokémon ha evolucionado a Godmode!")
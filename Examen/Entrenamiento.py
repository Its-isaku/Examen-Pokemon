#? Librerias
from abc import ABC, abstractmethod

#? Clase abstracta
class Entrenamiento(ABC):   #* Clase base de la que heredan los pokemones
    
    @abstractmethod   #* Método abstracto que sube el ataque del pokemon
    def subirAtaque(self):
        pass

    @abstractmethod  #* Método abstracto que sube la defensa del pokemon
    def subirDefensa(self):  
        pass

    @abstractmethod #* Método abstracto que sube la vida del pokemon.
    def subirVida(self):
        pass
    
    @abstractmethod #* Método abstracto que sube el nivel del pokemon.
    def subirNivel(self):
        pass


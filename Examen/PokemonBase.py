#? Librerias
from abc import ABC, abstractmethod

#? Clase abstracta
class Base(ABC):    #* Clase base de la que heredan los pokemones
    def __init__(self, nombre="N/A", nombreEv2="N/A", nombreEv3="N/A", desc="N/A", ataque=0, defensa=0, vida=0, level=1, evol=1, atrapado=False):
        #? Atributos encapsulados
        self._nombre = nombre
        self._nombreEv2 = nombreEv2
        self._nombreEv3 = nombreEv3
        self._desc = desc
        self._ataque = ataque
        self._defensa = defensa
        self._vida = vida
        self._level = level
        self._evol = evol
        self._atrapado = atrapado

    #? Getters y Setters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nombreEv2(self):
        return self._nombreEv
    
    @property
    def nombreEv3(self):
        return self._nombreEv

    @property
    def desc(self):
        return self._desc

    @property
    def ataque(self):
        return self._ataque

    @property
    def defensa(self):
        return self._defensa

    @property
    def vida(self):
        return self._vida

    @property
    def level(self):
        return self._level
    
    @property
    def evol(self):
        return self._evol

    @property
    def atrapado(self):
        return self._atrapado
    
    @vida.setter
    def vida(self, valor):
        self._vida = max(0, valor)    #* Asegura que la vida no sea negativa

    @atrapado.setter
    def atrapado(self, estado):
        self._atrapado = estado    #* Cambia el estado de atrapado

    #? Métodos abstractos
    @abstractmethod
    def hablar(self):   #* Método abstracto que imprime un mensaje del pokemon
        pass

    @abstractmethod
    def actualizar(self):   #* Método abstracto que actualiza los atributos del pokemon
        pass
    
    #? Método para actualizar nivel
    def actualizar_lvl(self):   #* Método que actualiza el nivel del pokemon
        if self._level >= 100 and self._evol < 3: 
            self._level = 1 #* Cuando llega al nivel 100 o más, regresa al nivel 1.
            self._evol += 1 #* Aumenta la evolución
            self._nombre = self._nombreEv2 if self._evol == 2 else self._nombreEv3 if self._evol == 3 else self._nombre #* Cambia el nombre del pokemon según la evolución
            
            print(f"Evolución: {self._evol}")  #* Mostrar el estado de la evolución

            if self._evol == 2:
                print("¡Tu Pokémon ha evolucionado! Forma intermedia")
                self._nombre = self._nombreEv2
            elif self._evol >= 3:
                print("¡Tu Pokémon ha evolucionado a Godmode! Forma final")
                self._nombre = self._nombreEv3
                
#? Métodos abstractos de Entrenamiento
    def subirAtaque(self):
        self._ataque += 5
        print(f"Ataque incrementado en 5. Nuevo ataque: {self._ataque}")

    def subirDefensa(self):
        self._defensa += 5
        print(f"Defensa incrementada en 5. Nueva defensa: {self._defensa}")

    def subirVida(self):
        self._vida += 10
        print(f"Vida incrementada en 10. Nueva vida: {self._vida}")
        
    def subirNivel(self):
        if self._evol < 3:
            self._level += 10
            print(f"Nivel incrementado en 10. Nuevo nivel: {self._level}")
            if self._level >= 100 and self._evol < 3:
                self.actualizar_lvl()  #* Llama al método de la clase base para manejar la evolución
        else:
            print(f"{self._nombre} ha alcanzado su maxima evolucion!")
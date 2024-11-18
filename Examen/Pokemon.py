'''
#! Ezequel Villa
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase Pokemon y sus metodos
'''
##? Librerias
from PokemonBase import Base

#? Clase concreta
class Pokemon(Base): #* Clase donde se definen los atributos de un pokemon
    
    #? Constructor
    def __init__(self, nombre="N/A", desc="N/A", ataque=0, defensa=0, vida=0, level=1, evol=1, atrapado=False):
        super().__init__(nombre, desc, ataque, defensa, vida, level, evol, atrapado)
        
    #? Método para mostrar los atributos del pokemon
    def detalles_pokemon(self): #* Método que imprime los atributos del pokemon
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self._level}")
        print(f"Evolución: {self._evol}")
        print(f"Atrapado: {'Sí' if self.atrapado else 'No'}")
        
    #?Getters y Setters
    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, value):
        self._defensa = value

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = value

    #? Métodos para hablar
    def hablar(self): #* Método que imprime un mensaje del pokemon
        print(f"¡{self.nombre}, {self.nombre}, {self.nombre}!")

    #? Método de actualización completa
    def actualizar(self, boost_ataque=10, boost_defensa=10, boost_vida=10): #* Método que actualiza todos los atributos del pokemon
        self._ataque += boost_ataque
        self._defensa += boost_defensa
        self._vida += boost_vida
        print(f"Atributos actualizados: \\nAtaque: {self._ataque} \\nDefensa: {self._defensa} \\nVida: {self._vida}")
    
    #? Método para entrenar
    def entrenar(self): #* Método que aumenta los atributos del pokemon
        self._ataque += 10
        self._defensa += 10
        self._vida += 10
        self._level += 5
        print(f"{self.nombre} ha entrenado! \nNivel actual: {self._level}\\n")
        if self._level >= 100:
            print(f"¡{self.nombre} ha evolucionado!")
            self._level = 0
            self._evol += 1

    #? Métodos de Entrenamiento
    def subirAtaque(self):
        self._ataque += 10
        print(f"Ataque incrementado en 5. Nuevo ataque: {self._ataque}")

    def subirDefensa(self):
        self._defensa += 10
        print(f"Defensa incrementada en 5. Nueva defensa: {self._defensa}")

    def subirVida(self):
        self._vida += 10
        print(f"Vida incrementada en 10. Nueva vida: {self._vida}")
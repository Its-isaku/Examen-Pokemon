##? Librerias
from PokemonBase import Base

#? Clase concreta
class Pokemon(Base): #* Clase donde se definen los atributos de un pokemon
    
    #? Constructor
    def __init__(self, nombre="N/A", nombreEv2="N/A", nombreEv3="N/A", desc="N/A", ataque=0, defensa=0, vida=0, level=1, evol=1, atrapado=False):
        super().__init__(nombre, nombreEv2, nombreEv3, desc, ataque, defensa, vida, int(level), evol, atrapado)
        
    #? Métodos para hablar
    def hablar(self): #* Método que imprime un mensaje del pokemon
        print(f"¡{self.nombre}, {self.nombre}, {self.nombre}!")

    #? Método para mostrar los atributos del pokemon
    def detalles_pokemon(self): #* Método que imprime los atributos del pokemon
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self._level}")
        print(f"Evolución: {self._evol}")
        print(f"Atrapado: {'Si\n' if self.atrapado else 'No\n'}")
        self.hablar()
        
    def detalles_pokemon_archivo(self): #* Método que imprime los atributos del pokemon
        detalles = (
        f"Nombre: {self.nombre}\n"
        f"Descripcion: {self.desc}\n"
        f"Ataque: {self.ataque}\n"
        f"Defensa: {self.defensa}\n"
        f"Vida: {self.vida}\n"
        f"Nivel: {self._level}\n"
        f"Evolucion: {self._evol}\n"
        f"Atrapado: {'Si' if self.atrapado else 'No'}\n")
        return detalles
        
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

    #? Método de actualización completa
    def actualizar(self, boost_ataque=10, boost_defensa=10, boost_vida=10, boost_lvl = 10): #* Método que actualiza todos los atributos del pokemon
        self._ataque += boost_ataque
        self._defensa += boost_defensa
        self._vida += boost_vida
        self._level += boost_lvl
        print(f"Atributos actualizados: \\nAtaque: {self._ataque} \\nDefensa: {self._defensa} \\nVida: {self._vida} \\nNivel: {self._level}")
        self.actualizar_lvl() #* llamar metodo de clase base para manejar evol
    
    #? Método para entrenar
    def entrenar(self): #* Método que aumenta los atributos del pokemon
        self._ataque += 10
        self._defensa += 10
        self._vida += 10
        self._level += 5
        print(f"{self.nombre} ha entrenado! \nNivel actual: {self._level}\\n")
        self.actualizar_lvl()

    #? Métodos de Entrenamiento con un boost +10
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
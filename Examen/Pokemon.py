
# Clase concreta
class Pokemon(PokemonBase):
    def detallesPokemon(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.level}")
        print(f"Evolución: {self.evol}")
        print(f"Atrapado: {'Sí' if self.atrapado else 'No'}")

    def hablar(self):
        print(f"{self.nombre} dice: ¡Pika Pika!")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.vida += 10
        self.level += 5
        print(f"{self.nombre} ha entrenado. Nivel actual: {self.level}")
        if self.level >= 100:
            print(f"¡{self.nombre} ha evolucionado!")
            self.level = 0
            self.evol += 1

    # Métodos de mejora
    def subirAtaque(self):
        self.ataque += 10
        print(f"Ataque aumentado. Nuevo ataque: {self.ataque}")

    def subirDefensa(self):
        self.defensa += 10
        print(f"Defensa aumentada. Nueva defensa: {self.defensa}")

    def subirVida(self):
        self.vida += 10
        print(f"Vida aumentada. Nueva vida: {self.vida}")

    # Método de actualización completa
    def actualizar(self, boost_ataque=10, boost_defensa=10, boost_vida=10):
        self.ataque += boost_ataque
        self.defensa += boost_defensa
        self.vida += boost_vida
        print(f"Atributos actualizados: Ataque: {self.ataque}, Defensa: {self.defensa}, Vida: {self.vida}")

# Ejemplo de uso
pikachu = Pokemon(nombre="Pikachu", desc="Pokémon eléctrico", ataque=55, defensa=40, vida=35)
pikachu.detallesPokemon()
pikachu.hablar()
pikachu.entrenar()
pikachu.subirAtaque()
pikachu.subirDefensa()
pikachu.subirVida()
pikachu.actualizar()  # Usa el método de actualización completa
pikachu.detallesPokemon()


# Examen Pokémon: Pokédex en Python

Este proyecto es parte de un examen diseñado para poner en práctica los conceptos de Programación Orientada a Objetos (POO) en Python. El objetivo principal es crear una **Pokédex interactiva**, que permita gestionar Pokémon con diversas funcionalidades como entrenamiento, combate, evolución y captura.

## Contexto

La Pokédex es una simulación que permite al usuario visualizar y gestionar Pokémon con habilidades específicas. Al final del proyecto, deberás tener un Pokémon que pueda:
- Ser entrenado.
- Evolucionar.
- Participar en combates.
- Capturar Pokémon enemigos.

## Funcionalidades Principales

1. **Clases Base y Abstractas:**
   - Implementación de una clase base abstracta `PokemonBase` con atributos predeterminados (nombre, ataque, defensa, vida, nivel, evolución) y métodos abstractos como `hablar()` y `actualizar()`.

2. **Clases Concretas y Especialización:**
   - Creación de una clase concreta `Pokemon` que implementa los métodos abstractos.
   - Especialización mediante subclases (Agua, Fuego, Eléctrico, Hierba) con atributos y métodos únicos.

3. **Interacción y Simulación:**
   - Sistema de combate donde los Pokémon compiten basándose en sus atributos.
   - Posibilidad de capturar Pokémon enemigos.
   - Entrenamiento de Pokémon mediante métodos específicos.

4. **Menú Interactivo:**
   - Interacción con el usuario mediante un menú que permite seleccionar, entrenar, y usar Pokémon en combates.
   - Persistencia hasta que el usuario decida finalizar.

## Estructura del Proyecto

El trabajo está dividido entre tres integrantes:

### Sofía
- Diseño y desarrollo de clases base abstractas.
- Creación de métodos y atributos esenciales.

### Ezequiel
- Implementación de la clase concreta `Pokemon`.
- Desarrollo de subclases especializadas por tipo de Pokémon (Agua, Fuego, etc.).

### Isai
- Creación del menú interactivo.
- Simulación de combate y sistema de captura.

## Requisitos Técnicos

- **Python 3.8 o superior**.
- Se requiere instalar la librería `random` (incluida en Python estándar).
- Documentación del código con comentarios breves y concisos.

## Este examen está diseñado para demostrar habilidades en:

- vHerencia.
- Polimorfismo.
- Encapsulamiento.
- Manejo de clases abstractas y especialización.

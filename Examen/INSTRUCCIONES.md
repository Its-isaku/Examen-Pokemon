
# Guia de Documentacion y Estilo de Codigo (PEP 8n)

## Encabezado obligatorio en cada archivo
Incluye este bloque al inicio de cada archivo para identificar al autor y la funcion principal:

```python
'''
 //! Nombre de integrante
 //? Grupo: 544
 //? Nombre de Profesor

 //* Breve repaso de lo que hara en el archivo
'''
```

### Ejemplo:

```python
'''
 //! Sofia
 //? Grupo: 544
 //? Profesor: Emanuel Gomez

 //* Este archivo implementa una calculadora que suma, resta, multiplica y divide.
'''
```

---

## Uso de Better Comments
Para organizar y entender el codigo, utiliza colores con Better Comments:

1. **//! - Titulos (Amarillo):** Para titulos o secciones principales.
   ```python
   //! Operaciones Matematicas
   ```

2. **//? - Subtitulos (Azul):** Para describir librerias, variables, metodos o secciones especificas.
   ```python
   //? Importacion de librerias
   ```

3. **//* - Explicaciones detalladas (Verde):** Para detallar lo que hace cada parte del codigo.
   ```python
   //* Este for itera sobre la lista y los imprime.
   for num in numeros:
       print(num)
   ```

---

## Reglas basicas para variables, metodos, clases y mas

### 1. Variables:
- Usa **snake_case** (minusculas y guiones bajos).
- **Ejemplo:**
  ```python
  nombre_usuario = "Gareth"
  ```

### 2. Metodos (Funciones):
- Usa **snake_case** y comenta su proposito.
- **Ejemplo:**
  ```python
  //? Calcula el area de un rectangulo
  def calcular_area_rectangulo(base, altura):
      return base * altura
  ```

### 3. Clases:
- Usa **CamelCase** para nombres.
- **Ejemplo:**
  ```python
  class Calculadora:
      //* Inicializa los valores
      def __init__(self, modelo):
          self.modelo = modelo
  ```

### 4. Constantes:
- Usa **mayusculas** con guiones bajos.
- **Ejemplo:**
  ```python
  PI = 3.14159
  ```

### 5. Archivos y Modulos:
- Usa **snake_case** para los nombres de archivos.
- **Ejemplo:**
  ```python
  calculos_matematicos.py
  ```

### 6. Identacion:
- Usa **4 espacios** por nivel.
- **Ejemplo:**
  ```python
  if condicion:
      print("Verdadero")
  ```

---

## Ejemplo completo de archivo Python:

```python
'''
 //! Gareth
 //? Grupo: 544
 //? Profesor: Profe Laura

 //* Calcula areas de figuras geometricas.
'''

//! Definicion de funciones
def calcular_area_circulo(radio):
    //* Calcula el area de un circulo dado su radio.
    return math.pi * radio ** 2

//! Programa principal
if __name__ == "__main__":
    //? Variables principales
    radio = float(input("Ingresa el radio del circulo: "))
    //* Llama a la funcion para calcular el area
    area = calcular_area_circulo(radio)
    print(f"Area: {area}")
```

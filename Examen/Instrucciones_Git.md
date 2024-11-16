# Guia Rapida: Comandos Basicos de Git

### 1. **Inicializar un repositorio Git**
Este comando crea un nuevo repositorio Git en el directorio actual.

```bash
git init
```
- Resultado: Se inicializa un repositorio vacio en `.git`.

---

### 2. **Agregar archivos al area de preparacion**
Anade los archivos que quieres incluir en tu proximo commit.

```bash
git add .
```
- `.`: Agrega todos los archivos modificados o nuevos al area de preparacion.

---

### 3. **Hacer un commit**
Guarda los cambios en el historial del repositorio con un mensaje descriptivo.

```bash
git commit -m "Descripcion del cambio"
```
- `-m`: Especifica el mensaje del commit.
- `"Descripcion del cambio"`: Un mensaje claro que describa lo que hiciste (ej. "Agregue archivo README.md").

---

### 4. **Subir los cambios al repositorio remoto (main)**
Sube los cambios al repositorio remoto en la rama principal.

```bash
git push origin main
```
- `origin`: El nombre del repositorio remoto (por defecto).
- `main`: La rama principal (puede ser diferente dependiendo de tu configuracion).

---
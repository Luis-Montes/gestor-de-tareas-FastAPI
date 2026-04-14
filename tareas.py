import json

archivo = "data.json"

def cargar_tareas():
    try:
        with open(archivo, "r") as datos:
            return json.load(datos)
    except:
        return []

def guardar_tarea(tareas):
    with open(archivo, "w") as datos:
        json.dump(tareas, datos)

def crear_tarea(nombre):
    tareas = cargar_tareas()

    nueva = {
        "nombre": nombre,
        "status": False
    }

    tareas.append(nueva)
    guardar_tarea(tareas)
    return nueva

def completar_tarea(indice):
    tareas = cargar_tareas()

    if indice < 0 or indice >= len(tareas):
        return None

    tareas[indice]["status"] = True
    guardar_tarea(tareas)

    return tareas[indice]

def eliminar_tarea(indice):
    tareas = cargar_tareas()
    
    if indice < 0 or indice >= len(tareas):
        return None
    
    eliminada = tareas.pop(indice)
    guardar_tarea(tareas)

    return eliminada
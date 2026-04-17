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

def crear_tarea(tarea):
    tareas_lista = cargar_tareas()

    if len(tareas_lista) == 0:
        nuevo_id = 1
    else:
        ultimo_id = max(t["id"] for t in tareas_lista)
        nuevo_id = ultimo_id + 1

    nueva = {
        "id": nuevo_id,
        "nombre": tarea.nombre,
        "status": tarea.status
    }

    tareas_lista.append(nueva)
    guardar_tarea(tareas_lista)

    return nueva

def completar_tarea(id, tarea):
    tareas_lista = cargar_tareas()

    for t in tareas_lista:
        if t["id"] == id:
            t["nombre"] = tarea.nombre
            t["status"] = tarea.status
            guardar_tarea(tareas_lista)
            return t

    
    return None


def eliminar_tarea(id):
    tareas = cargar_tareas()

    for i, t in enumerate(tareas):
        if t["id"] == id:
            eliminada = tareas.pop(i)
            guardar_tarea(tareas)
            return eliminada
    return None
from fastapi import FastAPI
import tareas

app = FastAPI()

@app.get("/")
def inicio():
    return {"Hello": "World"}

@app.get("/tareas")
def obtener_tareas():
    return tareas.cargar_tareas()


@app.post("/tareas")
def crear_tarea(nombre: str):
    return tareas.crear_tarea(nombre)

@app.put("/tareas/{indice}")
def completar_tarea(indice: int):
    return tareas.completar_tarea(indice)

@app.delete("/tareas/{indice}")
def eliminar_tarea(indice: int):
    return tareas.eliminar_tarea(indice)
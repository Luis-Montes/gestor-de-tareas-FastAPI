from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tareas

app = FastAPI()

class Tarea(BaseModel):
    nombre: str
    status: bool = False

@app.get("/")
def inicio():
    return {"Hello": "World"}

@app.get("/tareas")
def obtener_tareas():
    return tareas.cargar_tareas()


@app.post("/tareas")
def crear_tarea(nombre: Tarea):
    return tareas.crear_tarea(nombre)

@app.put("/tareas/{id}")
def completar_tarea(id: int, tarea: Tarea):
    resultado = tareas.completar_tarea(id, tarea)

    if resultado is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    return resultado



@app.delete("/tareas/{id}")
def eliminar_tarea(id: int):
    resultado =  tareas.eliminar_tarea(id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    return resultado
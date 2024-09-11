# API REST: Interfaz de programacion de aplicaciones para compartir recursos
from typing import List, Optional
import uuid
from fastapi import FastAPI
from pydantic import BaseModel

#inicializo una variable que tendra todas las caracteristicas de una API REST
app = FastAPI()

#Defino la clase modelo
class Curso(BaseModel):
    id: str
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int

# Ejemplo de base de datos
cursos_db = []

#CRUD: Read (lectura) metodo GET ALL:

#            URL
@app.get('/cursos/',response_model=list[Curso])
def obtener_cursos():
    return cursos_db

#CRUD: Create (Escribir) POST:
@app.post('/cursos/',response_model= Curso)
def crear_curso(curso:Curso):
    curso.id = str(uuid.uuid4())
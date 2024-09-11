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

#CRUD: Read (lectura) metodo GET en general:

#            URL
@app.get('/cursos/',response_model=list[Curso])
def obtener_cursos():
    return cursos_db

#CRUD: Create (Escribir) POST:
@app.post('/cursos/',response_model= Curso)
def crear_curso(curso:Curso):
    curso.id = str(uuid.uuid4()) # Uso UUID para generar un ID único
    cursos_db.append(curso)

#CRUD: Read (Lectura) metodo GET individual:
@app.get('/cursos/{curso_id}',response_model=Curso)
def obtener_curso(curso_id:str):
    curso = next((curso for curso in cursos_db if curso_id == curso_id),None) # con Next tomo la primera coincidencia
    if curso is None:
        raise Exception(status_code=404, detail='Curso no encontrado')
    return curso

#CRUD: Update ( Actualizar/modificar) PUT: Modificar un curso con el ID que se envie
@app.put('/cursos/{curso_id}',response_model=Curso)
def actualizar_curso(curso_id:str,curso_actualizado:Curso):
    curso = next((curso for curso in cursos_db if curso_id == curso_id),None) # con Next tomo la primera coincidencia
    if curso is None:
        raise Exception(status_code=404, detail='Curso no encontrado')
    curso_actualizado.id = curso.id
    index = cursos_db.index(curso) #Se busca el indice exacto en la lista de cursos
    cursos_db[index] = curso_actualizado
    return curso_actualizado

#CRUD: Delete(Borrar) DELETE: Se elimina un recurso con el ID que se envie
@app.delete('/cursos/{curso_id}',response_model=Curso)
def eliminar_curso(curso_id:str,curso_actualizado:Curso):
    curso = next((curso for curso in cursos_db if curso_id == curso_id),None) # con Next tomo la primera coincidencia
    if curso is None:
        raise Exception(status_code=404, detail='Curso no encontrado')
    cursos_db.remove(curso)
    return curso










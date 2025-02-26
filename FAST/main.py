from fastapi import FastAPI,HTTPException
from typing import Optional,List
from models import modeloUsuario

app= FastAPI(
    title='Mi primerAPI 192',
    description= 'Ivan Isay Guerra Lopez',
    version='1.0.1'
)

#BD ficticia
usuarios=[
    {"id": 1,"nombre":"ivan", "edad":37,"correo":"example@example.com"},
    {"id": 2,"nombre":"isay", "edad":15,"correo":"example2@example.com"},
    {"id": 3,"nombre":"petra", "edad":18,"correo":"example3@example.com"},
    {"id": 4,"nombre":"ana", "edad":37,"correo":"example4@example.com"}
]

#Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'world FastAPI'}

#Endpoint CONSULTA TODOS
@app.get('/todosUsuarios',response_model= List[modeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios


#Endpoint Agregar nuevos
@app.post('/usuario/',response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El id ya existe ")
    
    usuarios.append(usuario)
    return usuario    

#Endpoint para actualizar
@app.put('/usuarios/{id}',response_model= modeloUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]= usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400,detail="El usuario no existe") 
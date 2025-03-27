from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter


routerUsuario = APIRouter()


#Endpoint CONSULTA TODOS
@routerUsuario.get('/todosUsuario',tags=['Operaciones CRUD'])
def leerUsuarios():
    db= Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                      "Excepcion": str(e)   })
    finally:
        db.close()
        
        
#Endpoint buscar por id
@routerUsuario.get('/usuario/{id}',tags=['Operaciones CRUD'])
def buscarUno(id:int):
    db= Session()
    try:
        consultauno= db.query(User).filter(User.id == id).first()
        
        if not consultauno:
            return JSONResponse(status_code=404,content= {"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content= jsonable_encoder(consultauno))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                      "Excepcion": str(e)   })
    finally:
        db.close()
    
    
#Endpoint Agregar nuevos
@routerUsuario.post('/usuario/',response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    db= Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message":"Usuario Guardado",
                                      "usuario": usuario.model_dump()   })
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message":"Error al Guardar Usuario",
                                      "Excepcion": str(e)   })
    finally:
        db.close()    



#Endpoint para actualizar usuario
@routerUsuario.put('/usuario/{id}', response_model=modeloUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modeloUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Actualizar campos
        for key, value in usuarioActualizado.model_dump().items():
            setattr(usuario, key, value)

        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario actualizado", "usuario": usuarioActualizado.model_dump()})

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "No fue posible actualizar", "Error": str(e)})
    finally:
        db.close()


#Endpoint para eliminar usuario
@routerUsuario.delete('/usuario/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        db.delete(usuario)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado"})

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "No fue posible eliminar", "Error": str(e)})
    finally:
        db.close()
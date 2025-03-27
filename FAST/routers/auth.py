
from fastapi.responses import JSONResponse
from modelsPydantic import  modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from fastapi import APIRouter


routerAuth = APIRouter()

# ----------- Auth para generar el Token ----------------#  
   
#Endpoint Autenticacion
@routerAuth.post('/auth', tags=['Autentificacion'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == 'ivan@example.com' and autorizacion.passw == "123456789":
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return {"Aviso":"Usuario sin autorizacion"}
  

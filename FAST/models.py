
from pydantic import BaseModel, Field, EmailStr

#modelo de validaciones
class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0,description="Id unico y solo numeros positivos")
    nombre:str = Field(...,min_length=3, max_length=85,description="Solo letras: min 3 max 85 ")
    edad: int = Field(..., ge=1, le=121, description="Edad entre 1 y 121 años")
    correo: EmailStr = Field(..., description="Correo electrónico válido",example="correo@example.com")
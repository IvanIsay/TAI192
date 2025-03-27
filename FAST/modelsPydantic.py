
from pydantic import BaseModel, Field, EmailStr

#modelo de validaciones
class modeloUsuario(BaseModel):
    name:str = Field(...,min_length=3, max_length=85,description="Solo letras: min 3 max 85 ")
    age: int = Field(..., ge=1, description="Edad entre 1 y 121 años")
    email: EmailStr = Field(..., description="Correo electrónico válido",example="correo@example.com")
    
    
class modeloAuth(BaseModel):
    email:EmailStr = Field(..., description="Correo electrónico válido",example="correo@example.com") 
    passw: str = Field(..., min_length=8,strip_whitespace=True,description="Contraseña minimo 8 caracteres" )   
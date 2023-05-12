from pydantic import BaseModel, EmailStr, Field


class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=5, max_length=60)
    email: EmailStr


class UsuarioIn(UsuarioBase):
    senha: str = Field(..., min_length=8, max_length=20)


class UsuarioOut(UsuarioBase):
    id: int
    role: str

    class Config:
        orm_mode = True

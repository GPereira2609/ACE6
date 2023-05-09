from sqlalchemy.orm import Session
from app.utils import register
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut
from app.models.usuario import Usuario
from app.utils.register import get_hashed_password, verify_password
from fastapi import HTTPException

class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, user: UsuarioIn) -> UsuarioOut:
        if self.db.query(Usuario).filter(Usuario.email == user.email).first():
            return HTTPException(status_code=409, detail="E-mail já está sendo utilizado")
        else:
            senha_bd = get_hashed_password(user.senha)
            user_bd = Usuario(**user.dict(), senha=senha_bd)
            self.db.add(user_bd)
            self.db.commit()
            self.db.refresh()
       
        return user

    

    
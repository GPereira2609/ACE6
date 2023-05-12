from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut
from app.utils.auth import get_hashed_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, user: UsuarioIn) -> UsuarioOut:
        if self.db.query(Usuario).filter(Usuario.email == user.email).first():
            return HTTPException(status_code=409, detail="O usuário já está cadastrado")
        else:
            user_bd = Usuario(**user.dict(), senha=get_hashed_password(user.senha))
            self.db.add(user_bd)
            self.db.commit()
            self.db.refresh()

        return user

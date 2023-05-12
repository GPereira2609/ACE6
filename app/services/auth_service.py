from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut
from app.utils.auth import get_hashed_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, request: UsuarioIn) -> UsuarioOut:
        data = request.dict()

        user_exist = self.db.query(Usuario).filter_by(email=data['email']).all()

        if user_exist:
            raise HTTPException(status_code=409, detail="O usuário já está cadastrado")
        else:
            user_bd = Usuario(**{**data, "senha": get_hashed_password(data["senha"])})
            self.db.add(user_bd)
            self.db.commit()
            self.db.refresh(user_bd)

        return UsuarioOut(id=user_bd.id, email=user_bd.email, nome=user_bd.nome, role=user_bd.role)

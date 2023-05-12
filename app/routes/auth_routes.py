from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut
from app.services.auth_service import AuthService

auth_router = APIRouter()


@auth_router.post('/registrar', response_model=UsuarioOut)
def register(data: UsuarioIn, session: Session = Depends(get_db)):
    return AuthService(session).register(data)

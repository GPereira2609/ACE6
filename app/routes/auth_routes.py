from fastapi import APIRouter

from app.database.db import get_db
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut
from app.services.auth_service import AuthService

session = get_db()

auth_service = AuthService(session)

auth_router = APIRouter()


@auth_router.post('/registrar', response_model=UsuarioOut)
def register(data: UsuarioIn):
    return auth_service.register(data)

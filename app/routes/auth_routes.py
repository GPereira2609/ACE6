from fastapi import APIRouter
from app.services.auth_service import AuthService
from app.database.db import get_db
from app.schemas.UsuarioSchema import UsuarioIn, UsuarioOut

session = get_db()

auth_service = AuthService(session)

auth_router = APIRouter()

@auth_router.post(path='/registrar', response_model=UsuarioOut)
def registrar(data: UsuarioIn):
    return auth_service.register(data) 
from app.database.db import Base
from app.models.requisicao import Requisicao
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

class Usuario(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    nome = Column(String(60), nullable=False)
    senha = Column(String, nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    role = Column(String(60), nullable=False, default='user')

    usuario_aprovador = relationship("Requisicao", back_populates='usuario_aprovador')
    usuario_solicitante = relationship("Requisicao", back_populates='usuario_solicitante')

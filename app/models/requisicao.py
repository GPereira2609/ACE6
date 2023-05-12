from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

from app.database.db import Base


class Requisicao(Base):
    __tablename__ = 'requisicoes'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    nome_gerencia = Column(String(200), nullable=False)
    data_criacao = Column(TIMESTAMP, server_default=func.now())
    data_atualizacao = Column(TIMESTAMP, nullable=True)
    usuario_aprovador_id = Column(Integer, ForeignKey('usuarios.id'), nullable=True)
    usuario_aprovador = relationship("Usuario", back_populates="usuario_aprovador")
    usuario_solicitante_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    usuario_solicitante = relationship("Usuario", back_populates='usuario_solicitante')

    reservas = relationship("Reserva", back_populates='reservas')
    status = Column(String(20), nullable=False, default='pendente')

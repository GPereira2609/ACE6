from app.database.db import Base
from app.models.requisicao import Requisicao
from app.models.material import Material
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

class Reserva(Base):
    __tablename__ = 'reservas'

    solicitacao_id = Column(Integer, ForeignKey("requisicao.id"), primary_key=True)
    solicitacao = relationship("Requisicao", back_populates='solicitacao')
    material_id = Column(Integer, ForeignKey("materiais.id"), primary_key=True)
    material = relationship("Material", back_populates='material')
    quantidade = Column(Integer, nullable=False)
from app.database.db import Base
from app.models.estoque import Estoque
from app.models.reserva import Reserva
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

class Material(Base):

    __tablename__ = 'materiais'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    nome = Column(String(60), nullable=False)
    descricao = Column(String(120), nullable=True)

    estoque = relationship("Estoque", back_populates='estoque')
    reserva = relationship("Reserva", back_populates='reserva')
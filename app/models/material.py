from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class Material(Base):
    __tablename__ = 'materiais'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    nome = Column(String(60), nullable=False)
    descricao = Column(String(120), nullable=True)

    estoque = relationship("Estoque", back_populates='estoque')
    reserva = relationship("Reserva", back_populates='reserva')

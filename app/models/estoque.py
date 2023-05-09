from app.database.db import Base
from app.models.material import Material
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

class Estoque(Base):

    __tablename__ = 'estoques'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    quantidade = Column(Integer, nullable=False)
    material_id = Column(Integer, ForeignKey("materiais.id"))
from sqlalchemy import Column, Integer, ForeignKey

from app.database.db import Base


class Estoque(Base):
    __tablename__ = 'estoques'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    quantidade = Column(Integer, nullable=False)
    material_id = Column(Integer, ForeignKey("materiais.id"))

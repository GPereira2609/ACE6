from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: int           = Column(Integer, primary_key=True, index=True)
    nome: String      = Column(String(60), nullable=False)
    email: String     = Column(String(60), nullable=False)
    senha: String     = Column(String(60), nullable=False)
    permissao: String = Column(String(60), nullable=False, default='user')

    usuario_aprovador = relationship("Solicitacao", back_populates="usuario_aprovador")
    usuario_solicitante = relationship("Solicitacao", back_populates="usuario_solicitante")

class Material(Base):
    __tablename__ = "materiais"

    id: int           = Column(Integer, primary_key=True, index=True)
    nome: String      = Column(String(60), nullable=False)
    descricao: String = Column(String(100), nullable=False)

    estoque = relationship("Estoque", back_populates="material")
    reserva = relationship("Reserva", back_populates="material")

class Estoque(Base):
    __tablename__ = "estoques"

    id: int = Column(Integer, primary_key=True, index=True)
    quantidade: int = Column(Integer, nullable=False)
    material_id: int = Column(Integer, ForeignKey("materiais.id"))
    material = relationship("Material", back_populates="estoque")

class Solicitacao(Base):
    __tablename__ = "solicitacoes"

    id: int = Column(Integer, primary_key=True, index=True)
    nome_gerencia_curso: String = Column(String(200), nullable=False)
    data_criacao: TIMESTAMP = Column(TIMESTAMP, server_default=func.now())
    data_atualizacao: TIMESTAMP = Column(TIMESTAMP, nullable=True)
    usuario_aprovador_id: int = Column(Integer, ForeignKey('usuarios.id'), nullable=True)
    usuario_aprovador = relationship("Usuario", back_populates="usuario_aprovador")
    usuario_solicitante_id: int = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario_solicitante = relationship("Usuario", back_populates="usuario_solicitante")
    reservas = relationship("Reserva", back_populates="solicitacao")
    status: String = Column(String(20), nullable=False, default='pendente')

class Reserva(Base):
    __tablename__ = "reservas"

    solicitacao_id: int = Column(Integer, ForeignKey("solicitacoes.id"))
    solicitacao = relationship("Solicitacao", back_populates="reservas")    
    material_id: int = Column(Integer, ForeignKey("materiais.id"))
    material = relationship("Material", back_populates="reserva")
    quantidade: int = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("solicitacao_id", "material_id")
    )
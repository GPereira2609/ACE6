from sqlalchemy.orm import Session

from models import Usuario, Material, Estoque, Reserva, Solicitacao

class RepositorioUsuario:

    @staticmethod
    def find_by_id(db: Session, id: int) -> Usuario:
        return db.query(Usuario).filter(Usuario.id == id).first()
    
    @staticmethod
    def save_user(db: Session, usuario: Usuario) -> Usuario:
        if usuario.id:
            db.merge(usuario)
        else:
            db.add(usuario)
        db.commit()
        return usuario
    
    @staticmethod
    def delete_user_by_id(db: Session, id: int) -> None:
        curso = db.query(Usuario).filter(Usuario.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()

class RepositorioSolicitacao:

    @staticmethod
    def get_all(db: Session) -> list(Solicitacao):
        return db.query(Solicitacao).all()
    
    @staticmethod
    def get_by_solicitante_id(db: Session, id: int) -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.usuario_solicitante_id == id).all()
    
    @staticmethod
    def get_by_aprovador_id(db: Session, id: int) -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.usuario_aprovador_id == id).all()
    
    @staticmethod
    def get_by_nome_gerencia_curso(db: Session, gerencia: Solicitacao.nome_gerencia_curso) -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.nome_gerencia_curso == gerencia).all()
    
    @staticmethod
    def get_between_dates(db: Session, dt_inicio: Solicitacao.data_criacao, dt_fim: Solicitacao.data_atualizacao)  -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.data_criacao >= dt_inicio, Solicitacao.data_atualizacao <= dt_fim).all()
    
    @staticmethod
    def get_by_status(db: Session, status: Solicitacao.status) -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.status == status).all()
    
    @staticmethod
    def get_by_solic_id(db: Session, id: int) -> list(Solicitacao):
        return db.query(Solicitacao).filter(Solicitacao.id == id).all()
    
class RepositorioReserva:

    @staticmethod
    def get_by_solicitacao_id(db: Session, id: int) -> list(Reserva):
        return db.query(Reserva).filter(Reserva.solicitacao_id == id).all()
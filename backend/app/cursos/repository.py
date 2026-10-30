from typing import Optional, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlmodel import select, func as sql_func
from app.cursos.models import Curso

class CursoRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, curso_data: dict) -> Curso:
        nuevo_curso = Curso(**curso_data)
        self.db.add(nuevo_curso)
        self.db.commit()
        self.db.refresh(nuevo_curso)
        return nuevo_curso
    
    def get_by_id(self, curso_id: int) -> Optional[Curso]:
        statement = select(Curso).where(Curso.id == curso_id)
        return self.db.exec(statement).first()
    
    def listar_paginado(
        self,
        page: int = 1,
        size: int = 20,
        q: Optional[str] = None,
        categoria_id: Optional[int] = None
    )-> Tuple[List[Curso], int]:
        statement = select(Curso)

        if q:
            patron = f"%{q.strip()}%"
            statement = statement.where(
                (func.lower(Curso.titulo).like(func.lower(patron))) |
                (func.lower(Curso.tema).like(func.lower(patron)))
            )
        
        if categoria_id:
            statement = statement.where(Curso.categoria_id == categoria_id)
        
        count_statement = select(func.count()).select_from(statement.subquery())
        total = self.db.exec(count_statement).one()

        statement = statement.order_by(Curso.id.asc()).offset((page - 1)*size).limit(size)
        items = self.db.exec(statement).all()

        return items, total
    
    def update(self, curso_id: int, datos_actualizados: int) -> Optional[Curso]:
        curso = self.get_by_id(curso_id)
        if not curso:
            return None

        for clave, valor in datos_actualizados.items():
            if hasattr(curso, clave) and valor is not None:
                setattr(curso, clave, valor)

        self.db.commit()
        self.db.refresh(curso)
        return curso
    
    def delete(self, curso_id: int) -> bool:
        curso = self.get_by_id(curso_id)
        if not curso:
            return False
        
        self.db.delete(curso)
        self.db.commit()
        return True
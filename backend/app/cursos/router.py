from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.cursos.models import Curso

router = APIRouter(prefix="/cursos", tags=["cursos"])

@router.get("")
def listar_cursos_publicos(
    page: int = 1,
    size: int = 20,
    db: Session = Depends(get_session)
):
    statement = select(Curso).where(Curso.estado == "aprobado")
    cursos = db.exec(statement).all()
    
    return {
        "items": [{"id": c.id, "titulo": c.titulo, "estado": c.estado} for c in cursos],
        "total": len(cursos),
        "page": page,
        "page_size": size
    }

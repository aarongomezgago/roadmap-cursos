from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Header
from pydantic import BaseModel
from sqlmodel import Session

from app.database import get_session
from app.cursos.models import Curso
from app.aportes.service import validar_permiso_moderacion, evaluar_transicion_moderacion

router = APIRouter(prefix="/aportes", tags=["aportes"])

class AporteCreate(BaseModel):
    titulo: str
    tema: str
    url: str
    version: str
    anio_edicion: int
    docentes: str
    categoria_id: int
    tiene_cuestionarios: bool = False
    requiere_examen: bool = False
    extiende_certificado: bool = False
    aval_organizacion: Optional[str] = None
    declara_que_lo_tomo: bool

class ValidacionPayload(BaseModel):
    aprobado: bool
    motivo_rechazo: Optional[str] = None

def _obtener_rol_desde_token(authorization: Optional[str]) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Se requiere token de autenticación"
        )
    token = authorization.replace("Bearer ", "").strip()
    if token == "mock_token_admin":
        return "admin"
    return "user"

@router.post("", status_code=status.HTTP_201_CREATED)
def crear_aporte(
    payload: AporteCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_session)
):
    _obtener_rol_desde_token(authorization)

    nuevo_curso = Curso(
        titulo=payload.titulo,
        tema=payload.tema,
        url=payload.url,
        version=payload.version,
        anio_edicion=payload.anio_edicion,
        docentes=payload.docentes,
        categoria_id=payload.categoria_id,
        tiene_cuestionarios=payload.tiene_cuestionarios,
        requiere_examen=payload.requiere_examen,
        extiende_certificado=payload.extiende_certificado,
        aval_organizacion=payload.aval_organizacion,
        estado="pendiente"
    )
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)

    return {
        "id": nuevo_curso.id,
        "titulo": nuevo_curso.titulo,
        "estado": nuevo_curso.estado
    }

@router.post("/{aporte_id}/validar", status_code=status.HTTP_200_OK)
def validar_aporte(
    aporte_id: int,
    payload: ValidacionPayload,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_session)
):
    rol = _obtener_rol_desde_token(authorization)
    try:
        validar_permiso_moderacion(rol)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))

    curso = db.get(Curso, aporte_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aporte no encontrado")

    nuevo_estado = "aprobado" if payload.aprobado else "rechazado"
    try:
        evaluar_transicion_moderacion(
            estado_actual=curso.estado,
            nuevo_estado=nuevo_estado,
            motivo_rechazo=payload.motivo_rechazo
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    curso.estado = nuevo_estado
    db.add(curso)
    db.commit()
    db.refresh(curso)

    return {
        "id": curso.id,
        "titulo": curso.titulo,
        "estado": curso.estado
    }

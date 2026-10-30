from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, unique=True, index=True)
    descripcion: Optional[str] = Field(default=None, max_length=255)

class Curso(SQLModel, table=True):
    __tablename__ = "cursos"

    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(max_length=2048, unique=True, index=True)
    titulo: str = Field(max_length=200)
    tema: str = Field(max_length=100)
    version: str = Field(max_length=50)
    anio_edicion: int
    docentes: str
    tiene_cuestionarios: bool = Field(default=False)
    requiere_examen: bool = Field(default=False)
    extiende_certificado: bool = Field(default=False)
    aval_organizacion: Optional[str] = Field(default=None, max_length=150)
    categoria_id: int = Field(foreign_key="categorias.id", index=True)
    estado: str = Field(default="borrador", index=True)
    creado_en: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
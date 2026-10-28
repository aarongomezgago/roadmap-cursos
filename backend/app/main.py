from fastapi import FastAPI

app = FastAPI(
    title="Learnity API",
    version="0.1.0",
    description="API para catalogo y roadmaps de cursos"
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

@app.get("/api/v1/cursos", tags=["Cursos"])
def listar_cursos():
    return {
        "items": [
            {
                "id": 1,
                "url": "prueba.com",
                "titulo": "Curso Prueba 1",
                "tema": "Prueba",
                "version": "v2.0",
                "anio_edicion": 2026,
                "docentes": "Docente prueba 1",
                "tiene_cuestionarios": True,
                "requiere_examen": False,
                "extiende_certificado": True,
                "aval_organizacion": "UTN",
                "estado": "aprobado",
                "categoria": {"id": 1, "nombre": "Informatica"}
            },
            {
                "id": 2,
                "url": "prueba.com",
                "titulo": "Curso Prueba 2",
                "tema": "Prueba",
                "version": "v2.0",
                "anio_edicion": 2026,
                "docentes": "Docente prueba 2",
                "tiene_cuestionarios": False,
                "requiere_examen": True,
                "extiende_certificado": True,
                "aval_organizacion": "",
                "estado": "aprobado",
                "categoria": {"id": 2, "nombre": "Redes"}
            }
        ],
        "total": 1,
        "page": 1,
        "page_size": 20
    }
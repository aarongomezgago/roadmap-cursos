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
                "url": "aprender.com",
                "titulo": "Curso Prueba",
                "tema": "Prueba",
                "version": "v2.0",
                "anio_edicion": 2026,
                "docentes": "Docente prueba",
                "tiene_cuestionarios": True,
                "requiere_examen": False,
                "extiende_certificado": True,
                "aval_organizacion": "UTN",
                "estado": "aprobado",
                "categoria": {"id": 1, "nombre": "Informatica"}
            }
        ],
        "total": 1,
        "page": 1,
        "page_size": 20
    }
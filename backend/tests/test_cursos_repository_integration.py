import pytest
from app.cursos.repository import CursoRepository

def _datos_curso_base(titulo="Test", tema="Testing", categoria_id=1, url="https://www.test.com"):
    return {
        "titulo": titulo,
        "tema": tema,
        "url": url,
        "version": "v1.0",
        "anio_edicion": 2024,
        "docentes": "Docente test",
        "categoria_id": categoria_id,
        "estado": "aprobado",
        "tiene_cuestionarios": True,
        "requiere_examen": False,
        "extiende_certificado": True,
    }

def test_create_and_get_by_id_roundtrip(db_session):
    repo = CursoRepository(db_session)
    datos = _datos_curso_base("Prueba", "Testing", url="https://www.learnity.com")

    curso_creado = repo.create(datos)
    curso_recuperado = repo.get_by_id(curso_creado.id)

    assert curso_recuperado is not None
    assert curso_recuperado.id == curso_creado.id
    assert curso_recuperado.titulo == "Prueba"

def test_listado_paginado_retorna_items_y_conteo_correcto(db_session):
    repo = CursoRepository(db_session)
    repo.create(_datos_curso_base("Curso 1", "Tema 1", url="https://www.curso1.com"))
    repo.create(_datos_curso_base("Curso 2", "Tema 2", url="https://www.curso2.com"))
    repo.create(_datos_curso_base("Curso 3", "Tema 3", url="https://www.curso3.com"))

    items_p1, total_p1 = repo.listar_paginado(page=1, size=2)
    items_p2, total_p2 = repo.listar_paginado(page=2, size=2)

    assert total_p1 == 3
    assert len(items_p1) == 2
    assert items_p1[0].titulo == "Curso 1"
    assert items_p1[1].titulo == "Curso 2"

    assert total_p2 == 3
    assert len(items_p2) == 1
    assert items_p2[0].titulo == "Curso 3"

def test_filtros_busqueda_q_case_insensitive_y_categoria(db_session):
    repo = CursoRepository(db_session)
    repo.create(_datos_curso_base("Desarrollo", "Tema 4", categoria_id=1, url="https://www.curso4.com"))
    repo.create(_datos_curso_base("Curso 5", "Tema 5", categoria_id=1, url="https://www.curso5.com"))
    repo.create(_datos_curso_base("Curso 6", "Tema 6", categoria_id=2, url="https://www.curso6.com"))

    items_q, total_q = repo.listar_paginado(q="dEsArRollO")
    items_cat, total_cat = repo.listar_paginado(categoria_id=2)

    assert total_q == 1
    assert items_q[0].titulo == "Desarrollo"

    assert total_cat == 1
    assert items_cat[0].titulo == "Curso 6"

def test_update_campos_parciales_y_delete(db_session):
    repo = CursoRepository(db_session)
    curso = repo.create(_datos_curso_base("Curso", "Tema", url="https://www.curso.com"))

    curso_actualizado = repo.update(curso.id, {"titulo": "Testing", "anio_edicion": 2026})

    assert curso_actualizado.titulo == "Testing"
    assert curso_actualizado.anio_edicion == 2026
    assert curso_actualizado.tema == "Tema"

    exito_delete = repo.delete(curso.id)
    curso_borrado = repo.get_by_id(curso.id)

    assert exito_delete is True
    assert curso_borrado is None
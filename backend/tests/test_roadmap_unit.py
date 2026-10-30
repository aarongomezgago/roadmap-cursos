import pytest
from app.roadmap.service import (
    agregar_curso_a_roadmap,
    quitar_curso_de_roadmap,
    reordenar_roadmap,
)

# Tests agregar curso

def test_agregar_curso_a_roadmap_camino_feliz_agrega_y_asigna_posicion():
    roadmap_inicial = []
    curso_aprobado = {"id": 10, "titulo": "Curso test", "estado": "aprobado"}

    resultado = agregar_curso_a_roadmap(roadmap_inicial, curso_aprobado)

    assert len(resultado) == 1
    assert resultado[0]["curso_id"] == 10
    assert resultado[0]["posicion"] == 1
    assert resultado[0]["estado_progreso"] == "pendiente"

def test_agregar_curso_a_roadmap_curso_inexistente_lanza_exception():
    roadmap = []
    curso = None

    with pytest.raises(ValueError) as exc_info:
        agregar_curso_a_roadmap(roadmap, curso)

    assert "no existe" in str(exc_info.value)

def test_agregar_curso_a_roadmap_curso_no_aprobado_lanza_exception():
    roadmap = []
    curso_pendiente = {"id": 11, "titulo": "Curso no aprobado", "estado": "pendiente"}

    with pytest.raises(ValueError) as exc_info:
        agregar_curso_a_roadmap(roadmap, curso_pendiente)

    assert "estado 'aprobado'" in str(exc_info.value)

def test_agregar_curso_a_roadmap_curso_duplicado_lanza_exception():
    curso_id = 10
    roadmap_existente = [{"curso_id": curso_id, "posicion": 1, "estado_progreso": "pendiente"}]
    curso_mismo_id = {"id": curso_id, "titulo": "Curso duplicado", "estado": "aprobado"}

    with pytest.raises(ValueError) as exc_info:
        agregar_curso_a_roadmap(roadmap_existente, curso_mismo_id)

    assert "ya se encuentra en tu roadmap" in str(exc_info.value)

# Tests quitar curso

def test_quitar_curso_de_roadmap_camino_feliz_recalcula_posiciones():
    roadmap_inicial = [
        {"curso_id": 101, "posicion": 1, "estado_progreso": "completado"},
        {"curso_id": 102, "posicion": 2, "estado_progreso": "pendiente"},
        {"curso_id": 103, "posicion": 3, "estado_progreso": "pendiente"},
    ]

    resultado = quitar_curso_de_roadmap(roadmap_inicial, curso_id=102)

    assert len(resultado) == 2
    assert resultado[0]["curso_id"] == 101
    assert resultado[0]["posicion"] == 1
    assert resultado[1]["curso_id"] == 103
    assert resultado[1]["posicion"] == 2

def test_quitar_curso_de_roadmap_curso_inexistente_lanza_exception():
    roadmap = [{"curso_id": 101, "posicion": 1, "estado_progreso": "pendiente"}]

    with pytest.raises(ValueError) as exc_info:
        quitar_curso_de_roadmap(roadmap, curso_id=999)

    assert "no se encuentra en el roadmap" in str(exc_info.value)

# Tests reordenar roadmap

def test_reordenar_roadmap_camino_feliz_actualiza_posiciones():
    roadmap_original = [
        {"curso_id": 1, "posicion": 1, "estado_progreso": "completado"},
        {"curso_id": 2, "posicion": 2, "estado_progreso": "pendiente"},
        {"curso_id": 3, "posicion": 3, "estado_progreso": "pendiente"},
    ]
    nuevo_orden = [3, 1, 2]

    resultado = reordenar_roadmap(roadmap_original, nuevo_orden)

    assert resultado[0]["curso_id"] == 3 and resultado[0]["posicion"] == 1
    assert resultado[1]["curso_id"] == 1 and resultado[1]["posicion"] == 2
    assert resultado[2]["curso_id"] == 2 and resultado[2]["posicion"] == 3

def test_reordenar_roadmap_ids_invalidos_lanza_exception():
    roadmap_original = [
        {"curso_id": 1, "posicion": 1, "estado_progreso": "pendiente"},
        {"curso_id": 2, "posicion": 2, "estado_progreso": "pendiente"},
    ]
    nuevo_orden_invalido = [1, 99]

    with pytest.raises(ValueError) as exc_info:
        reordenar_roadmap(roadmap_original, nuevo_orden_invalido)

    assert "no coincide con los cursos" in str(exc_info.value)
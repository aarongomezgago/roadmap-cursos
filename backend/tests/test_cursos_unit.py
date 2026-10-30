import pytest
from app.cursos.service import validar_transicion_estado, validar_aporte_curso

# Tests transicion estados

def test_validar_transicion_estado_camino_feliz_retorna_true():
    estado_actual = "borrador"
    nuevo_estado = "pendiente"

    resultado = validar_transicion_estado(estado_actual, nuevo_estado)

    assert resultado is True

def test_validar_transicion_estado_aprobado_a_pendiente_lanza_exception():
    estado_actual = "aprobado"
    nuevo_estado = "pendiente"

    with pytest.raises(ValueError) as exc_info:
        validar_transicion_estado(estado_actual, nuevo_estado)
    
    assert "Transicion invalida" in str(exc_info.value)

def test_validar_transicion_estado_borrador_a_aprobado_lanza_exception():
    estado_actual = "borrador"
    nuevo_estado = "aprobado"

    with pytest.raises(ValueError) as exc_info:
        validar_transicion_estado(estado_actual, nuevo_estado)

    assert "Transicion invalida" in str(exc_info.value)

def test_validar_transicion_estado_estado_inexistente_lanza_exception():
    estado_actual = "borrador"
    nuevo_estado = "publicado"  # estado no contemplado

    with pytest.raises(ValueError) as exc_info:
        validar_transicion_estado(estado_actual, nuevo_estado)

    assert "Estado no reconocido" in str(exc_info.value)


# Tests validacion aporte cursos

def test_validar_aporte_curso_camino_feliz_retorna_true():
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": "https://www.test.com",
        "version": "v1.0",
        "anio_edicion": 2024,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": True
    }
    urls_existentes = {"https://www.aprender.com"}

    resultado = validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert resultado is True

def test_validar_aporte_curso_url_formato_invalido_lanza_exception():
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": "ftp://testing.com",
        "version": "v1.0",
        "anio_edicion": 2024,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": True
    }
    urls_existentes = {"https://www.aprender.com"}

    with pytest.raises(ValueError) as exc_info:
        validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert "La URL debe comenzar con http:// o https://" in str(exc_info.value)

def test_validar_aporte_curso_url_duplicada_lanza_exception():
    url_repetida = "https://www.aprender.com"
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": url_repetida,
        "version": "v1.0",
        "anio_edicion": 2024,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": True
    }
    urls_existentes = {url_repetida}

    with pytest.raises(ValueError) as exc_info:
        validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert "ya se encuentra registrada" in str(exc_info.value)

def test_validar_aporte_curso_no_tomo_curso_retorna_true():
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": "https://www.test.com",
        "version": "v1.0",
        "anio_edicion": 2024,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": False
    }
    urls_existentes = {"https://www.aprender.com"}

    resultado = validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert resultado is True

def test_validar_aporte_curso_anio_futuro_lanza_exception():
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": "https://www.test.com",
        "version": "v1.0",
        "anio_edicion": 2030,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": True
    }
    urls_existentes = {"https://www.aprender.com"}

    with pytest.raises(ValueError) as exc_info:
        validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert "El año de edicion debe estar entre" in str(exc_info.value)

def test_validar_aporte_curso_anio_antiguo_lanza_exception():
    datos = {
        "titulo": "Test",
        "tema": "Informatica",
        "url": "https://www.test.com",
        "version": "v1.0",
        "anio_edicion": 1800,
        "docentes": "Docente test",
        "categoria_id": 1,
        "declara_que_lo_tomo": True
    }
    urls_existentes = {"https://www.aprender.com"}

    with pytest.raises(ValueError) as exc_info:
        validar_aporte_curso(datos, urls_existentes, anio_actual=2026)

    assert "El año de edicion debe estar entre" in str(exc_info.value)
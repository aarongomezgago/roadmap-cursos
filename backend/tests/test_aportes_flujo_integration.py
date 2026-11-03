import pytest
from fastapi.testclient import TestClient

def _auth_header(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}

# Aporte valido -> estado 'pendiente'
def test_crear_aporte_valido_queda_en_estado_pendiente(client: TestClient, token_usuario_comun: str):
    payload_aporte = {
        "titulo": "Testing",
        "tema": "Prueba",
        "url": "https://www.aprender.com",
        "version": "2024",
        "anio_edicion": 2024,
        "docentes": "Docente Test",
        "categoria_id": 1,
        "tiene_cuestionarios": True,
        "requiere_examen": False,
        "extiende_certificado": True,
        "aval_organizacion": "UTN",
        "declara_que_lo_tomo": True
    }

    response = client.post(
        "/api/v1/aportes",
        json=payload_aporte,
        headers=_auth_header(token_usuario_comun)
    )

    assert response.status_code == 201
    datos = response.json()
    assert datos["estado"] == "pendiente"
    assert datos["titulo"] == "Testing"

# Validar aprobado → curso aprobado y visible en GET /cursos
def test_validar_aprobado_pasa_curso_a_aprobado_y_visible_en_catalogo(
    client: TestClient, 
    token_usuario_comun: str, 
    token_admin: str
):
    # Usuario comun aporta un curso
    payload_aporte = {
        "titulo": "Nuevo Curso",
        "tema": "Informatica",
        "url": "https://www.nuevocurso.com",
        "version": "v2",
        "anio_edicion": 2024,
        "docentes": "Docente nuevo",
        "categoria_id": 1,
        "tiene_cuestionarios": True,
        "requiere_examen": False,
        "extiende_certificado": True,
        "aval_organizacion": "UTN",
        "declara_que_lo_tomo": True
    }
    res_aporte = client.post(
        "/api/v1/aportes", 
        json=payload_aporte, 
        headers=_auth_header(token_usuario_comun)
    )
    aporte_id = res_aporte.json()["id"]

    # Admin aprueba el aporte
    res_val = client.post(
        f"/api/v1/aportes/{aporte_id}/validar",
        json={"aprobado": True},
        headers=_auth_header(token_admin)
    )
    assert res_val.status_code == 200
    assert res_val.json()["estado"] == "aprobado"

    # Verificar que aparezca en el catalogo
    res_catalogo = client.get("/api/v1/cursos")
    assert res_catalogo.status_code == 200
    titulos_catalogo = [c["titulo"] for c in res_catalogo.json()["items"]]
    assert "Nuevo Curso" in titulos_catalogo

# Validar rechazado -> No visible en catalogo
def test_validar_rechazado_no_aparece_en_catalogo_publico(
    client: TestClient, 
    token_usuario_comun: str, 
    token_admin: str
):
    # Usuario aporta un curso no valido
    payload_aporte = {
        "titulo": "Curso spam",
        "tema": "Varios",
        "url": "https://www.cursospam.com",
        "version": "v1",
        "anio_edicion": 2023,
        "docentes": "Desconocido",
        "categoria_id": 1,
        "tiene_cuestionarios": True,
        "requiere_examen": False,
        "extiende_certificado": True,
        "aval_organizacion": "UTN",
        "declara_que_lo_tomo": False
    }
    res_aporte = client.post(
        "/api/v1/aportes", 
        json=payload_aporte, 
        headers=_auth_header(token_usuario_comun)
    )
    aporte_id = res_aporte.json()["id"]

    # Admin rechaza e indica motivo
    res_val = client.post(
        f"/api/v1/aportes/{aporte_id}/validar",
        json={"aprobado": False, "motivo_rechazo": "El enlace no presenta contenido educativo"},
        headers=_auth_header(token_admin)
    )
    assert res_val.status_code == 200
    assert res_val.json()["estado"] == "rechazado"

    # Verificar que no aparezca en catalogo
    res_catalogo = client.get("/api/v1/cursos")
    titulos_catalogo = [c["titulo"] for c in res_catalogo.json()["items"]]
    assert "Curso spam" not in titulos_catalogo

# Permisos: validador sin rol -> 403; autor sin sesion -> 401
def test_permiso_validador_sin_rol_admin_retorna_403(client: TestClient, token_usuario_comun: str):
    # Usuario comun intenta validar un aporte (ID ficticio 1)
    response = client.post(
        "/api/v1/aportes/1/validar",
        json={"aprobado": True},
        headers=_auth_header(token_usuario_comun)
    )

    assert response.status_code == 403

def test_autor_sin_sesion_al_intentar_aportar_retorna_401(client: TestClient):
    # Peticion sin sesion
    payload = {
        "titulo": "Curso Anonimo",
        "url": "https://www.cursoanonimo.com",
        "tema": "Test",
        "version": "1.0",
        "anio_edicion": 2024,
        "docentes": "-",
        "categoria_id": 1,
        "tiene_cuestionarios": True,
        "requiere_examen": False,
        "extiende_certificado": True,
        "aval_organizacion": "UTN",
        "declara_que_lo_tomo": True
    }

    response = client.post("/api/v1/aportes", json=payload)

    assert response.status_code == 401

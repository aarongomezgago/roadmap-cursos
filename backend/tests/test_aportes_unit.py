import pytest
from app.aportes.service import (
    validar_permiso_moderacion,
    evaluar_transicion_moderacion,
)

# Tests permisos moderacion

def test_validar_permiso_moderacion_admin_retorna_true():
    assert validar_permiso_moderacion("admin") is True

def test_validar_permiso_moderacion_usuario_comun_lanza_exception():
    rol = "user"

    with pytest.raises(ValueError) as exc_info:
        validar_permiso_moderacion(rol)

    assert "PERMISO_DENEGADO" in str(exc_info.value)

def test_validar_permiso_moderacion_rol_nulo_lanza_exception():
    with pytest.raises(ValueError) as exc_info:
        validar_permiso_moderacion(None)

    assert "PERMISO_DENEGADO" in str(exc_info.value)

# Tests transicion de estados

def test_evaluar_transicion_moderacion_aprobar_pendiente_exitoso():
    estado_actual = "pendiente"
    nuevo_estado = "aprobado"

    resultado = evaluar_transicion_moderacion(estado_actual, nuevo_estado)

    assert resultado is True

def test_evaluar_transicion_moderacion_rechazar_con_motivo_exitoso():
    estado_actual = "pendiente"
    nuevo_estado = "rechazado"
    motivo = "URL rota y curso no disponible"

    resultado = evaluar_transicion_moderacion(estado_actual, nuevo_estado, motivo_rechazo=motivo)

    assert resultado is True

def test_evaluar_transicion_moderacion_rechazar_sin_motivo_lanza_exception():
    estado_actual = "pendiente"
    nuevo_estado = "rechazado"
    motivo_vacio = "   "

    with pytest.raises(ValueError) as exc_info:
        evaluar_transicion_moderacion(estado_actual, nuevo_estado, motivo_rechazo=motivo_vacio)

    assert "RECHAZO_SIN_MOTIVO" in str(exc_info.value)

def test_evaluar_transicion_moderacion_re_evaluar_curso_ya_aprobado_lanza_exception():
    estado_actual = "aprobado"
    nuevo_estado = "rechazado"

    with pytest.raises(ValueError) as exc_info:
        evaluar_transicion_moderacion(estado_actual, nuevo_estado, motivo_rechazo="Motivo posterior")

    assert "TRANSICION_INVALIDA" in str(exc_info.value)
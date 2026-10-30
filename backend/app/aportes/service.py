from typing import Dict, Any, Optional

ROLES_MODERADORES = {"admin"}
ESTADOS_MODERABLES = {"pendiente"}
ESTADOS_FINALES = {"aprobado", "rechazado"}

def validar_permiso_moderacion(rol_usuario: Optional[str]) -> bool:
    """
    Verifica si un usuario tiene el rol admin para moderar aportess
    """
    if not rol_usuario or rol_usuario.lower() not in ROLES_MODERADORES:
        raise ValueError("PERMISO_DENEGADO: Solo usuarios con rol 'admin' pueden moderar aportes")
    return True

def evaluar_transicion_moderacion(
    estado_actual: str, 
    nuevo_estado: str, 
    motivo_rechazo: Optional[str] = None
) -> bool:
    """
    Valida los cambio de estado de un aporte a revisar:
    - Solo se pueden moderar aportes en estado 'pendiente'
    - El destino debe ser 'aprobado' o 'rechazado'
    - Si se rechaza, el motivo es obligatorio
    """
    if estado_actual not in ESTADOS_MODERABLES:
        raise ValueError(
            f"TRANSICION_INVALIDA: El aporte ya fue evaluado (estado actual: '{estado_actual}')"
        )

    if nuevo_estado not in ESTADOS_FINALES:
        raise ValueError(
            f"ESTADO_DESTINO_INVALIDO: '{nuevo_estado}' no es un estado valido, solo APROBADO o RECHAZADO"
        )

    if nuevo_estado == "rechazado":
        if not motivo_rechazo or not motivo_rechazo.strip():
            raise ValueError("RECHAZO_SIN_MOTIVO: Debe especificar el motivo del rechazo")

    return True
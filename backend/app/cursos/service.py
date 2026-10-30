from datetime import datetime
from typing import Set, Dict, Any

# Estados definidos en BackendSchema §2
ESTADOS_VALIDOS = {"borrador", "pendiente", "aprobado", "rechazado"}

TRANSICIONES_PERMITIDAS = {
    "borrador": {"pendiente"},
    "pendiente": {"aprobado", "rechazado"},
    "aprobado": set(),
    "rechazado": set()
}

def validar_transicion_estado(estado_actual: str, nuevo_estado: str) -> bool:
    """
    Valida si el cambio de estado es permitido segun reglas del dominio:
    - borrador -> pendiente
    - pendiente -> aprobado o rechazado
    """
    if estado_actual not in ESTADOS_VALIDOS or nuevo_estado not in ESTADOS_VALIDOS:
        raise ValueError(f"Estado no reconocido. Validos: {ESTADOS_VALIDOS}")

    permitidos = TRANSICIONES_PERMITIDAS.get(estado_actual, set())
    if nuevo_estado not in permitidos:
        raise ValueError(
            f"Transicion invalida: no se puede pasar de '{estado_actual}' a '{nuevo_estado}'"
        )
    return True

def validar_aporte_curso(
    datos_curso: Dict[str, Any], 
    urls_existentes: Set[str],
    anio_actual: int = None
) -> bool:
    """
    Valida los datos de un aporte de curso segun reglas de negocio:
    - Campos obligatorios no vacios
    - Formato basico de URL (http:// o https://)
    - URL no duplicada
    - Declaracion de toma del curso por el usuario
    - Año de edicion coherente
    """
    if anio_actual is None:
        anio_actual = datetime.now().year

    # Campos obligatorios
    campos_obligatorios = [
        "titulo", "tema", "url", "version", 
        "anio_edicion", "docentes", "categoria_id", "declara_que_lo_tomo"
    ]
    for campo in campos_obligatorios:
        valor = datos_curso.get(campo)
        if valor is None or (isinstance(valor, str) and not valor.strip()):
            raise ValueError(f"El campo '{campo}' es obligatorio")

    # Formato URL
    url = datos_curso.get("url", "").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("La URL debe comenzar con http:// o https://")

    # URL duplicada
    if url in urls_existentes:
        raise ValueError("La URL del curso ya se encuentra registrada en la plataforma")

    # Año de edicion coherente
    anio = datos_curso.get("anio_edicion", 0)
    if not isinstance(anio, int) or anio < 1990 or anio > anio_actual:
        raise ValueError(f"El año de edicion debe estar entre 1990 y {anio_actual}")

    return True
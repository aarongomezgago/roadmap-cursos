from typing import List, Dict, Any, Optional

def agregar_curso_a_roadmap(
    roadmap: List[Dict[str, Any]], 
    curso: Optional[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Agrega un curso al roadmap del usuario.
    Reglas de negocio:
    - El curso debe existir
    - El curso debe estar en estado 'aprobado'
    - No se permiten cursos duplicados en el mismo roadmap
    """
    if curso is None:
        raise ValueError("El curso no existe")

    if curso.get("estado") != "aprobado":
        raise ValueError("Solo se pueden agregar al roadmap cursos que estén en estado 'aprobado'")

    curso_id = curso.get("id")
    if any(item["curso_id"] == curso_id for item in roadmap):
        raise ValueError("El curso ya se encuentra en tu roadmap")

    nueva_posicion = len(roadmap) + 1
    nuevo_item = {
        "curso_id": curso_id,
        "posicion": nueva_posicion,
        "estado_progreso": "pendiente"
    }

    return roadmap + [nuevo_item]

def quitar_curso_de_roadmap(roadmap: List[Dict[str, Any]], curso_id: int) -> List[Dict[str, Any]]:
    """
    Elimina un curso del roadmap y reajusta las posiciones
    """
    if not any(item["curso_id"] == curso_id for item in roadmap):
        raise ValueError("El curso a eliminar no se encuentra en el roadmap")

    roadmap_filtrado = [item for item in roadmap if item["curso_id"] != curso_id]

    # Reindexar posiciones
    for index, item in enumerate(roadmap_filtrado, start=1):
        item["posicion"] = index

    return roadmap_filtrado

def reordenar_roadmap(roadmap: List[Dict[str, Any]], nuevo_orden_ids: List[int]) -> List[Dict[str, Any]]:
    """
    Reordena las posiciones de los cursos presentes segun lista de IDs recibida
    """
    ids_actuales = [item["curso_id"] for item in roadmap]

    if set(ids_actuales) != set(nuevo_orden_ids) or len(ids_actuales) != len(nuevo_orden_ids):
        raise ValueError("La lista de IDs no coincide con los cursos presentes en el roadmap")

    mapa_items = {item["curso_id"]: item for item in roadmap}

    roadmap_reordenado = []
    for posicion, curso_id in enumerate(nuevo_orden_ids, start=1):
        item = mapa_items[curso_id].copy()
        item["posicion"] = posicion
        roadmap_reordenado.append(item)

    return roadmap_reordenado
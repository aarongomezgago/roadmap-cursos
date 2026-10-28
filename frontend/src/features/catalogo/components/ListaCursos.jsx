import { useState, useEffect } from 'react'
import { getCursos } from '../api'

export function ListaCursos() {
  const [cursos, setCursos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    getCursos()
      .then((data) => {
        setCursos(data.items || [])
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  if (loading) return <p className="state-message">Cargando cursos del catálogo...</p>
  
  if (error) return (
    <div className="state-error">
      <p><strong>Error al conectar con la API:</strong> {error}</p>
    </div>
  )

  if (cursos.length === 0) return <p className="state-message">No hay cursos disponibles en este momento.</p>

  return (
    <ul className="cursos-list">
      {cursos.map((curso) => (
        <li key={curso.id} className="curso-card">
          <div className="curso-header">
            <h2>{curso.titulo}</h2>
            {curso.categoria?.nombre && (
              <span className="chip-categoria">{curso.categoria.nombre}</span>
            )}
          </div>

          <p className="curso-meta">
            <strong>Año:</strong> {curso.anio_edicion} ({curso.version}) | <strong>Docentes:</strong> {curso.docentes}
          </p>

          <p className="curso-url">
            <a
              href={curso.url.startsWith('http') ? curso.url : `https://${curso.url}`}
              target="_blank"
              rel="noopener noreferrer"
              >
                Link del curso
            </a>
          </p>

          <div className="curso-badges">
            {curso.tiene_cuestionarios && <span className="badge-atributo">Tiene cuestionarios ✔</span>}
            {curso.requiere_examen && <span className="badge-atributo">Requiere examen ✔</span>}
            {curso.extiende_certificado && <span className="badge-atributo">Extiende certificado ✔</span>}
            {curso.aval_organizacion && (<span className="badge-atributo">Avalado por: {curso.aval_organizacion}</span>)}
            <span className="badge-estado">{curso.estado}</span>
          </div>
        </li>
      ))}
    </ul>
  )
}
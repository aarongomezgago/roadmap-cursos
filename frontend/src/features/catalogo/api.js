export async function getCursos() {
  const res = await fetch('/api/v1/cursos')
  if (!res.ok) {
    throw new Error(`Error HTTP: ${res.status}`)
  }
  return res.json()
}
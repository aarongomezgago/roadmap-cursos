import { ListaCursos } from '../features/catalogo/components/ListaCursos'
import './App.css'

export default function App() {
  return (
    <main className="container">
      <h1 className="title">Learnity — Catálogo Comunitario</h1>
      <ListaCursos />
    </main>
  )
}
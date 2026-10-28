# Learnity

> WebApp de gestión de comunidad de cursos: catálogo comunitario de cursos gratuitos + roadmaps personales de aprendizaje.
>
> **Estado:** 📚 Instancia B — arranque del desarrollo

**Stack:** React 19 + Vite + pnpm · FastAPI + uv · PostgreSQL 18.6 · Docker Compose (dev)

## Como levantar

---

## Qué hace

**Learnity** es una plataforma colaborativa diseñada para estudiantes y autodidactas que buscan un espacio que centralice cursos gratuito de la web. Resuelve la dispersión de recursos mediante un catálogo comunitario validado, donde cualquier usuario autenticado puede aportar. A partir de este catálogo público, cada usuario puede consultar el contenido y vincularlo a su propio **roadmap personal de aprendizaje** para tener un seguimiento estructurado de sus metas educativas.

## Documentación

| Documento | Responde la pregunta | Link |
|-----------|----------------------|------|
| SPEC | ¿Qué nos pidieron construir y qué decidimos nosotros? | [docs/SPEC.md](docs/SPEC.md) |
| PRD | ¿Para quién, qué problema resuelve, qué hace y qué NO hace? | [docs/PRD.md](docs/PRD.md) |
| TRD | ¿Cómo lo construimos técnicamente y por qué? | [docs/TRD.md](docs/TRD.md) |
| UX-UI | ¿Cómo se ve, se siente y se comporta? | [docs/UX-UI.md](docs/UX-UI.md) |
| APPFlow | ¿Qué pantallas hay y cómo se navega? | [docs/APPFlow.md](docs/APPFlow.md) |
| BackendSchema | ¿Qué datos persistimos y qué API expone? | [docs/BackendSchema.md](docs/BackendSchema.md) |
| Implementation Plan | ¿En qué orden construimos y qué significa "hecho"? | [docs/IMPLEMENTATION_PLAN.md](docs/IMPLEMENTATION_PLAN.md) |

## Cómo revisar este repo

- Los `.md` se renderizan solos en GitHub.
- Los diagramas Mermaid (`erDiagram`, `flowchart`, `stateDiagram`) también: si los ves como
  texto crudo, falta el bloque ` ```mermaid `.
- Preview local: VS Code con `Ctrl+Shift+V` (extensión "Markdown All in One" recomendada).

## Estado del trabajo

| Instancia | Contenido | Estado |
|-----------|-----------|--------|
| A — Documentación | repo + 7 documentos | ✅ enviada a aprobación el 24/10/2026 |
| B — Desarrollo del MVP | ejecución del Implementation Plan | ⏳ en desarrollo |
| C — Clase 27/10 | testing, Docker multi-stage, gestión del cambio | ⏳ |

## Versionado

- **Flujo de Git:** Trunk-based development con ramas cortas por documento/módulo y Pull Requests/merges directos hacia `main`. Detalle en [TRD §4](docs/TRD.md#4-convenciones).
- **Convención de commits:** Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `docker:`, `refactor:`, `chore:`)

---

## Referencias de aprendizaje

### Markdown (para escribir los 6 documentos bien)

| Recurso | Para qué |
|---------|----------|
| [Markdown Guide — sintaxis básica](https://www.markdownguide.org/basic-syntax/) | encabezados, listas, énfasis, imágenes |
| [Markdown Guide — cheat sheet](https://www.markdownguide.org/cheat-sheet/) | tablas, task lists, bloques de código |
| [CommonMark — referencia](https://commonmark.org/help/) | la especificación cuando hay dudas |
| [GitHub — Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github) | GFM, tablas, checklists |
| [GitHub — Mermaid en Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | diagramas que renderizan en tu repo |

### Por tipo de documento

| Documento | Recurso |
|-----------|---------|
| PRD | [Atlassian — Plantilla PRD](https://www.atlassian.com/software/confluence/templates/product-requirements) · [Lenny Rachitsky — plantilla](https://www.atlassian.com/software/confluence/templates/requirements) |
| TRD | [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) — el clásico: contexto, goals/non-goals, trade-offs |
| UX-UI | [NN/g — Front-End Style-Guides](https://www.nngroup.com/articles/front-end-style-guides/) · [NN/g — Design Systems 101](https://www.nngroup.com/articles/design-systems-101/) · [Material Design 3 (la inspiración)](https://m3.material.io/) · [Material Symbols (iconos)](https://fonts.google.com/icons) |
| APPFlow | [NN/g — IA vs. Sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/) · [NN/g — User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/) |
| BackendSchema | [Mermaid — ER Diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) · [PostgreSQL — Conceptual Model](https://www.postgresql.org/docs/current/datamodel.html) |
| Implementation Plan | [Atlassian — Plantilla de plan de proyecto](https://www.atlassian.com/software/confluence/templates/project-plan) · [Shape Up](https://basecamp.com/shapeup/) — scopes y ciclos |

---

## Licencia / uso

Trabajo Práctico — Desarrollo de Software, UTN FR La Plata, 2026.

# TRD — Technical Requirements Document — Learnity

## 1. Stack y versiones exactas

| Capa | Elección | Versión exacta | Por qué |
|------|----------|----------------|---------|
| Frontend | React + Vite + pnpm | react 19.x, vite x.y, pnpm 12.14 | UI declaratva y moderna integrada con herramientra de build rápida y gestor de paquetes eficiente basado en hard links. |
| Backend | FastAPI + uv | fastapi 0.158.2, uv 0.13.4 | Framework REST de alto rendimiento con validación nativa y gestor de paquetes rápido. |
| ORM / driver | SQLModel + psycopg | | Simplifica la definición de schemas y el acceso a PostgreSQL |
| BD | PostgreSQL | 18.6 | fijado por SPEC |
| Infra (dev) | Docker + Compose | 24.0.7 | Garantiza aislamiento de entornos y poder replicar exactamente servicios entre desarrolladores. |

## 2. Decisiones técnicas

| # | Decisión | Alternativas consideradas | Elegida | Por qué |
|---|----------|---------------------------|---------|---------|
| TD-001 | Estrategia de autenticación | JWT stateless / sesión server-side / OAuth externo | JWT stateless | Permite desacoplar totalmente el cliente SPA en React de FastAPI sin tener que almacenar la sesión en el servidor. |
| TD-002 | Estrategia de paginación | offset + total / cursor-based | Offset + total | Facilita la navegación directa a páginas específicas en frontend y permite calcular y devolver el total de páginas. |
| TD-003 | Formato de errores de API | envelope propio / RFC 7807 (problem+json) | Envelope propio (`{ "error": { "code", "message", "details" } }`) | Respuestas de error homogéneas con exception handler en FastAPI facilitan que el frontend muestre mensajes claros. |
| TD-004 | Modelado de roadmap" | tabla intermedia con estado / referencia directa | Tabla intermedia | Permite registrar y actualizar metadatos para cada curso dentro de la trayectoria individual del usuario |

## 3. Arquitectura

### 3.1 Patrón y capas

Screaming Architecture + arquitectura en capas:

```mermaid
flowchart LR
    HTTP[HTTP / Controllers] --> SVC[Services — lógica de negocio]
    SVC --> REPO[Repositories — acceso a datos]
    REPO --> DB[(PostgreSQL)]
    SVC --> MODELS[Models / entidades]
```

- **Controllers:** reciben HTTP, validan input, delegan. Sin lógica de negocio.
- **Services:** reglas de negocio puras y testeables (sin BD, sin HTTP).
- **Repositories:** única puerta a la BD. Sin reglas de negocio.
- **La estructura de carpetas habla del dominio**, no del framework.

### 3.2 Estructura de carpetas

```
roadmap-cursos/
├── backend/
│   ├── pyproject.toml
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── auth/                       # registro, login, tokens, recuperacion
│   │   │   ├── router.py               # endpoints
│   │   │   ├── service.py              # reglas de negocio
│   │   │   ├── repository.py           # acceso a datos
│   │   │   └── models.py               # entidades / schemas
│   │   ├── cursos/                     # catálogo de cursos publicados
│   │   ├── aportes/                    # carga de cursos, flujo de moderación
│   │   ├── roadmap/                    # gestion de roadmap personal
│   │   └── categorias/                 # lista de categorias de cursos
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── Dockerfile
│   └── src/
│       ├── main.jsx
│       ├── app/                        # shell, router, layout global
│       ├── features/
│       │   ├── catalogo/               # vista de catálogo paginado y detalle
│       │   │   ├── components/
│       │   │   ├── hooks/
│       │   │   └── api.js
│       │   ├── aportar/                # formulario de aporte de cursos
│       │   ├── roadmap/                # interfaz del roadmap
│       │   ├── auth/                   # login y registro de usuarios
│       │   └── moderacion/             # panel de administración y aprobación
│       └── styles/                     # tokens globales (de UX-UI)
├── docker-compose.yml
└── docs/
```

### 3.3 Servicios Docker (entorno de desarrollo)

| Servicio | Imagen/base | Puerto | Rol |
|----------|-------------|--------|-----|
| postgres | postgres:18.6 | 5432 | base de datos |
| backend | python:3.x-slim + uv | 8000 | API FastAPI (dev) |
| frontend | node:20-alpine + pnpm | 5173 | SPA Vite (dev server) |

```mermaid
flowchart LR
    BROWSER[Navegador :5173] --> FE[frontend Vite]
    FE -- "/api/*" --> BE[backend FastAPI :8000]
    BE --> PG[(postgres :5432)]
```

## 4. Convenciones

- **Commits:** Conventional Commits — `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `docker:`
- **Flujo de Git:**
  - La rama `main` contiene solo código estable e integrable.
  - El trabajo se realiza en ramas cortas por tarea o historias de usuario que deriva del `main` (ej: `feat/us-001/[nombre-rama]`)
  - La inetgración a `main` se hace mediante Pull Requests o merges directos.
- **Errores de API:** Envelope unificado según `TD-003`:
    ```json
    {
      "error": {
        "code": "CURSO_DUPLICADO",
        "message": "La URL ingresada ya se encuentra registrada",
        "details": {
          "field": "url",
          "value": "[suspicious link removed]"
        }
      }
    }
    ```
- **Variables de entorno:**

  | Variable | Ejemplo | Obligatoria | Descripción |
  |----------|---------|-------------|-------------|
  | DATABASE_URL | postgresql://user:pass@postgres:5432/learnity_db | sí | cadena de conexión a la base de datos PostgreSQL |
  | SECRET_KEY | supersecretkey_learnity_2026_chang_me | sí | clave secreta para la firma de tokens JWT |
  | ALGORITHM | HS256 | sí | algoritmo de encriptación para tokens JWT |
  | ACCES_TOKEN_EXPIRE_MINUTES | 60 | sí | tiempo de expiración de las sesiones JWT en minutos |
  | ENVIRONMENT | development | no | entorno de ejecución (development, testing, production)
  | CORS_ORIGINS | http://localhost:5173 | sí | lista de orígenes permitidos en peticiones frontend/backend |

- **Logging y excepciones:**
  - **Logging**: Se utiliza módulo estandar logging de Python en nivel INFO para entornos de desarrollo y ERROR para fallos críticos, registrando peticiones fallidas (HTTP 4xx/5xx) y eventos de seguridad/autenticación.
  - **Excepciones**: Se capturan de manera global mediante exception handler en FastAPI, transformando cualquier fallo no controlado o HTTPException en formato estándar de la API.


## 5. Requisitos no funcionales técnicos (traducción de las restricciones)

| Restricción (SPEC) | Cómo se cumple | Dónde se verifica |
|--------------------|----------------|-------------------|
| Paginación de listados | Offset + total  | `GET /api/v1/cursos`, `GET /api/v1/roadmap` / componente Paginador en frontend (UX-UI $4.4) |
| Mobile-first con mejora progresiva | tokens + breakpoints documentados en UX-UI §3 | Tokens CSS en `frontend/src/styles`, prueba de inspección responsive, guía UX-UI $3 |
| Menú sándwich | componente Header con ARIA | Componentes Header y Drawer en `frontend/src/app`, ficha de navegación en APPFlow §3 y UX-UI $4.5 |
| Screaming Architecture | árbol §3.2 | Estructura de directorios según $3.2 |
| Seguridad en autenticación y rate limiting | Hash de contraseñas con bycrypt y protección contra ataques de fuerza bruta con rate limiting en login | `backend/app/auth` y prueba de llamadas concurrentes a `POST /api/v1/auth/login` |  

## 6. Riesgos técnicos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Validación y disponibilidad de URLs | media | medio | Validar sintaxis y formato de URL en línea en FastAPI, delegando la verificación de disponibilidad de enlace al Administrador en panel de moderación |
| Registros duplicados o condiciones de carrera en carga concurrente de enlaces | media | alto | Aplicar restricción a nivel de base de datos en PostgreSQL en la columna url en tabla cursos |
| Degradación del rendimiento de búsquedas y filtros combinados | baja | alto | Crear índices compuestos en PostgreSQL sobre las columnas 'estado, categoria_id' y búsqueda por texto, garantizando paginación estricta de 20 ítems por página. |
| Inconsistencia de layout o desborde en dispositivos móviles | media | medio | Implementar la estrategia de mejora progresiva declarando estilos base sin media queries y utilizando tokens CSS globales |

---

**Referencia:**
- Design Docs at Google (el clásico de los design docs, con énfasis en trade-offs):
  https://www.industrialempathy.com/posts/design-docs-at-google/

# SPEC — Learnity: WebApp de Gestión de Comunidad de Cursos

## 1. Identidad del producto

- **Learnity**
- **Permite a una comunidad de estudiantes colaborar en la creación de un catálogo de cursos gratuitos y gestionar su aprendizaje con roadmaps personales, fortaleciendo la organización y validación de contenido educativo confiable.**

## 2. Problema

Hoy en día, estudiantes o profesionales que buscan capacitarse, pueden enfrentarse a un problema al momento de buscar contenido educativo en plataformas o proveedores de internet: la falta de un espacio que pueda reunir y organizar dicho contenido de manera eficiente. A su vez, aquellos que buscan tener una hoja de ruta (o roadmap) de su aprendizaje sobre los cursos que realizan, generalmente lo hacen por su cuenta.

Si bien se pueden encontrar cursos en sitios como listas en blogs o foros, generalmente presentan información desactualizada o incompleta, enlaces rotos y falta de validación. El estudiante pierde tiempo buscando por su cuenta detalles como si el curso requiere examen, si otorga certificado o si está avalado por alguna organización. Por otro lado, existen herramientas para crear rutas de avance, pero estas son independientes.

Una comunidad cambia la ecuación del catálogo de cursos, ya que la colaboración, aporte y validación entre los propios usuarios garantiza calidad, una búsqueda más fina y una actualización constante del contenido. Si a eso se le suma la herramienta de roadmaps y la posibilidad de tener un catálogo personal, se tiene un espacio que resuelve ambas problemáticas y permite un seguimiento real del aprendizaje de cada estudiante.

## 3. Visión

En 12 meses, **Learnity** se consolidará como un espacio de referencia para la autoformación educativa libre, respaldado por su comunidad para mantener un catálogo amplio, confiable y lo más actualizado posible. Sus herramientas de roadmaps y catálogos personales facilita al estudiante tener a disposición sus metas de aprendizaje. De esta manera, Learnity ayuda a que cada vez más personas puedan acceder de manera rápida y efectiva a la información que ellos buscan y tener un seguimiento real de su progreso.

## 4. Alcance

### Dentro

1. **Roadmap personal de aprendizaje**: Cada usuario crea y gestiona su propio roadmap de curso, agregue cursos desde el catálogo comunitario y gestione el seguimiento/estado de su aprendizaje.
2. **Aporte de cursos:** El usuario carga cursos gratuitos de cualquier plataforma o proveedor, indicando su enlace web activo y, como mínimo:
   - categoría / rubro (seleccionado de una lista)
   - tema
   - título
   - versión
   - año de edición
   - docentes o disertantes que lo imparten
   - ¿cuenta con cuestionarios?
   - ¿requiere examen?
   - ¿extiende certificado?
   - ¿lo avala una organización?
3. **Declaración de toma**: Marcador donde el usuario que aporta un curso declara si lo tomó o no.
4. **Catálogo comunitario**: Todo curso aportado y **validado** pasa al catálogo comunitario; desde allí, cualquier usuario puede incluirlo en su catálogo / roadmap personal.
5. **Cuenta de usuario y autenticación**:
   - registro de usuario;
   - login;
   - recuperación de contraseña (ciclo completo: solicitud → token → nueva contraseña);
   - protección del **login con rate limiting**;
   - contraseñas cifradas con **bcrypt**


### Fuera (out of scope explícito)

- **Reproducción o alojamiento de contenido multimedia**: No se almacenan ni reproducen videos, audios o documentos dentro de la plataforma; únicamente se redirige mediante el enlace externo activo proporcionado.
- **Procesamiento de pagos o monetización**: La plataforma está orientada exclusivamente a cursos de acceso gratuito; no se integran pagos o suscripciones.
- **Integración automática con APIs externas**: No se sincroniza el progreso del usuario de forma automática con plataformas de terceros; el usuario es quien manualmente marca como completos sus avances en el curso.
- **Aplicación móvil nativa (iOS / Android)**: El producto es estrictamente una WebApp responsive diseñada bajo el enfoque **mobile-first**.
- **Interacción social avanzada**: No se incluyen foros de discusión, salas de chat en vivo, comentarios en tiempo real o sistemas de seguidores entre usuarios.

## 5. Reglas de producto clave

| # | Regla | Origen |
|---|-------|--------|
| BR-001 | Un curso aportado entra al sistema "en revisión" y solo llega al catálogo comunitario tras validación | SPEC clase ("cursos cargados y **validados** pasan al catálogo") |
| BR-002 | Cada usuario ve y edita solo su propio roadmap | Decisión propia |
| BR-003 | Quien aporta un curso declara si él/ella lo tomó | SPEC clase |
| BR-004 | Solo se permite la carga de cursos 100% gratuitos que cuenten con un enlace web activo funcional | SPEC clase |
| BR-005 | No se permiten aportes duplicados que compartan el mismo enlace web de un curso ya existente | Decisión propia |

## 6. Stack registrado (versiones exactas con las que se va a desarrollar)

| Capa | Tecnología | Versión exacta instalada |
|------|------------|--------------------------|
| Frontend | React + Vite + pnpm | react 19.x, vite x.y, pnpm 12.14 |
| Backend | FastAPI + uv | fastapi 0.158.2, uv 0.13.4 |
| Base de datos | PostgreSQL | [18.6] |
| Infra (dev) | Docker + Docker Compose | 24.0.7 |

## 7. Restricciones técnicas heredadas de la SPEC de clase

| # | Restricción | Cómo la vamos a cumplir (1-2 líneas) |
|---|-------------|--------------------------------------|
| 1 | Mobile-first con mejora progresiva: base sin media queries; `@media (min-width: …)` solo para agregar/mejorar | Estilos CSS base redactados exclusivamente para móviles. Se aplicará \`@media (min-width: ...)\` únicamente para adaptar a escritorio. |
| 2 | Paginación de todas las consultas de listado y de sus tablas | Paginación basada en desplazamiento (offset+total) — ver TRD §5 |
| 3 | Menú sándwich en mobile | Menú lateral desplegable en la barra de navegación para móvil, que pasa a ser barra horizontal en escritorio. |
| 4 | Screaming Architecture | Carpetas agrupadas por dominio — ver TRD §3.2 |

## 8. Vacíos de la SPEC de clase y decisiones tomadas

| # | Vacío detectado en la SPEC | Opciones consideradas | Decisión | Dónde se desarrolla |
|---|----------------------------|-----------------------|----------|---------------------|
| 1 | ¿Quién y cómo se validan los cursos aportados? | Validación por moderador / puntuación/votos de la comunidad | Un Administrador revisa un curso aportado en estado 'pendiente' y aprueba el contenido, pasando el mismo al estado 'aprobado' | PRD BR-001 / PRD US-005 / BackendSchema §3 |
| 2 | ¿Hay roles? | Rol único / Estudiante y Administrador | Dos roles definidos: Estudiante (aporta cursos, guarda en catálogo personal, crea y gestiona su roadmap) y Administrador (modera cursos pendientes y administra la WebApp) | PRD §3 y §7 / Backend §2 |
| 3 | ¿Qué es exactamente "incluir en mi catálogo"? | Añadir un curso a un listado personal | Un Estudiante puede añadir un curso del catálogo general de su interés en su catálogo personal | PRD US-003 / BackendSchema §2 / AppFlow §3 |
| 4 | ¿Cómo funciona la búsqueda? | Solo texto / solo filtros / ambos | Se puede buscar tanto por texto (título, tema) como por filtros (por categoría, año, características) | PRD US-004 / BackendSchema §4 / AppFlow §3 |
| 5 | ¿Cómo se evita la duplicación de cursos? | Administrador revisa manualmente / Restringir enlace único en base de datos | Se aplica la restricción para que un enlace sea único; si la URL ya se encuentra registrada, se rechaza el aporte | PRD BR-005 / BackendSchema §2 |

## 9. Historia de la SPEC (autoregistro de cambios)

| Fecha | Cambio | Por qué |
|-------|--------|---------|
| 20/10/2026 | SPEC de clase recibida en el aula | — |
| 21/10/2026 | Primer commit: SPEC de clase tal cual | regla de la consigna |
| 23/10/2026 | Refinamiento: agregación de Problema, Visión, Fuera de alcance y Vacíos de la SPEC original; suma de reglas de producto y restricciones técnicas | Completar la SPEC según plantilla |

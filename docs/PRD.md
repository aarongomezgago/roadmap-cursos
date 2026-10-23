# PRD — Product Requirements Document — Learnity

## 1. Resumen ejecutivo

**Learnity** es una plataforma web colaborativa para el aprendizaje autodidacta, donde estudiantes y profesionales pueden consultar y aportar a un catálogo comunitario de cursos gratuitos de diferentes proveedores. La aplicación permite a los usuarios asociar cursos del catálogo en una hoja de ruta (**roadmap**) personal para tener un seguimiento real de su trayecto de aprendizaje. 

## 2. Objetivos y métricas de éxito

| Objetivo | Cómo sabemos que lo logramos |
|----------|------------------------------|
| Que el catálogo comunitario tenga cursos validados de múltiples plataformas | Al menos un 80% de los cursos aportados son moderados por administradores; al menos 5 categorías distintas |
| Que el roadmap sea usado para planificar | Al menos la mitad de los usuarios tiene 1 curso asociado a su roadmap activo |
| Garantizar la integridad de datos | El 100% de los cursos publicados cumplen con los metadatos obligatorios completos |
| Evitar redundancias en el catálogo | No hay registros de enlaces duplicados en la base de datos |
| Brindar experiencia fluida y accesible desde dispositivos móviles | Cumplimiento de los criterios de enfoque **mobile-first** ; tiempo de carga del catálogo paginado inferior a 2 segundos |

## 3. Personas

### Persona 1 — Estudiante que busca orientarse

- **Contexto:** Estudiante universitario de 21 años que busca reforzar sus conocimientos y capacitarse más de un tema o área en sus ratos libres pero no sabe por donde empezar.
- **Motivaciones:** Encontrar cursos gratuitos con buena calidad de información y no perder tiempo con contenido viejo.
- **Frustraciones hoy:** Encuentra miles de cursos dispersos en Google o YouTube, sin saber cuál le conviene o si está vigente, y abandona su búsqueda.
- **Historias tipo:**
  - "Estuve buscando cursos de redes pero me aparecieron un montón de resultados y la verdad no se bien cuáles son confiables o no"
  - "Me gustaría poder tener en un solo lado los links e info de los cursos que me pueden llegar a servir"

### Persona 2 — Estudiante avanzada que recomienda cursos
- **Contexto**: Estudiante avanzada y autodidacta de 25 años a la que le piden recomendaciiones de cursos en grupos de estudio de WhatsApp o Discord.
- **Motivaciones**: Poder compartir cursos gratuitos que ya haya realizado sin tener que estar mandándolo varias veces o buscando un mensaje para reenviar un link.
- **Frustraciones hoy**: Algunos enlaces se rompen, los mensajes se pierden en la nada, o si llega a armar una planilla la gente ni la mira.
- **Historias tipo**:
  - "Me piden info de cursos que hice, pero a veces tengo que estar buscando para acordarme el link o toda la información"
  - "Estuve recomendando algunos de los cursos que fui haciendo pero a veces me lo vuelven a pedir porque se les pierden los mensajes; había armado un Excel para tener los links listados pero hace un tiempo que no lo actualicé."

## 4. User stories

| ID | Prioridad | Historia | Criterios de aceptación |
|----|-----------|----------|-------------------------|
| US-001 | P0 | Como visitante, quiero ver el catálogo comunitario paginado, para descubrir cursos sin registrarme | - [ ] Dado que visito `/catalogo`, veo la primera página (20 items)<br>- [ ] Dado que hay más de 20 cursos, aparece el paginador<br>- [ ] Dado que no hay cursos, veo un empty state con CTA |
| US-002 | P0 | Como visitante, quiero registrarme para acceder a las funcionalidades personales | - [ ] Dado que completo el formulario de registro con email y contraseña, la cuenta se crea exitosamente.<br>- [ ] Dado que intento registrarme con email ya registrado, el sistema muestra un error sin duplicar la cuenta.<br>- [ ] Dado que ingreso credenciales correctas en el login, el sistema genera la sesión y me redirige a mi panel. |
| US-003 | P0 |  Como usuario registrado, quiero aportar un curso con sus metadatos, para enriquecer el catálogo | - [ ] Dado que completo el formulario de aporte con su enlace, metadatos y declaro si tomé el curso, el mismo ingresa en estado 'Pendiente'<br>- [ ] Dado que el enlace ingresado ya existe en la base de datos, el sistema rechaza la carga del aporte e informa la duplicación.<br> - [ ] Dado que falta algún campo obligatorio, el formulario bloquea el envío e informa el error |
| US-004 | P0 | Como usuario registrado quiero agregar cursos del catálogo a mi roadmap personal y gestionar su progreso para seguir el avance de mi aprendizaje | - [ ] Dado que presiono "Agregar a mi roadmap" en un curso del catálogo, este se vincula a mi roadmap personal.<br> - [ ] Dado que acceso a mi roadmap, puedo modificar el avance de un curso asociado.<br>- [ ] Dado que elimino un curso de mi roadmap, este de desvincula sin borrar el curso del catálogo. |
| US-005 | P1 | Como administrador, quiero revisar el listado de cursos pendientes para aprobarlos o rechazarlos | - [ ] Dado que inicio sesión como Administrador y visito la sección de moderación, veo la lista paginada de cursos en estado 'Pendiente'.<br>- [ ] Dado que hago click en "Aprobar", el curso cambia a estado 'Aprobado' y se publica en el catálogo.<br>- [ ] Dado que hago click en "Rechazar", el curso cambia a estado 'Rechazado' y queda excluido del catálogo. |
| US-006 | P1 | Como usuario, quiero buscar cursos por texto libre y filtrarlos por categoría o atributos, para encontrar de manera rápida el contenido que necesito | - [ ] Dado que ingreso un texto en el buscador, el listado filtra cursos por coincidencia en título o tema.<br> - [ ] Dado que selecciono una categoría o activo el filtro "Otorga certificado", el catálogo muestra únicamente los cursos que coinciden.<br>- [ ] Dado que aplico filtros y no existen resultados, el sistema muestra un estado vacío con la opción de limpiar filtros. |

## 5. Requisitos funcionales

| ID | Requisito | Historia relacionada |
|----|-----------|----------------------|
| RF-001 | El sistema permite registrar usuarios con email y contraseña | US-002 |
| RF-002 | El sistema permite el inicio de sesión y autenticación de usuarios mediante tokens. | US-002 |
| RF-003 | El sistema permite la consulta pública y paginada del catálogo de cursos aprobados (20 ítems por página) | US-001 |
| RF-004 | El sistema ermite a usuarios autenticados aportar un curso con enlace activo y metadatos oblligatoruos, ingresando en estado 'Pendiente' | US-003 |
| RF-005 | El sistema valida que la URL del curso aportado sea única en a base de datos, rechazando la carga de un curso con URL ya registrado. | US-003 |
| RF-006 | El sistema permite a usuarios autenticados agregar cursos del catálogo a su roadmap personal y gestionar su avance | US-004 |
| RF-007 | El sistema ofrece a usuarios administradores una interfaz de moderación para revisar cursos en estado 'Pendiente' | US-005 |
| RF-008 | El sistema permite buscar cursos por texto y aplicar filtros. | US-006 |

## 6. Requisitos no funcionales

| ID | Requisito | Notas |
|----|-----------|-------|
| RNF-001 | Todos los listados paginados | heredado de SPEC clase |
| RNF-002 | Mobile-first con mejora progresiva | heredado de SPEC clase |
| RNF-003 | Seguridad y protección en el login mediante límite de tasa de peticiones (rate limiting). | heredado de SPEC clase |
| RNF-004 | Almacenamiento seguro de credenciales utilizando bycript como mínimo para las contraseñas | heredado de SPEC clase |
| RNF-005 | Arquitectura del código estructurada por dominio | heredado de SPEC clase |
| RMF-006 | Tiempo de respuesta del catálogo paginado inferior a 2 segundos para garantizar una navegación fluida | Decisión propia |

## 7. Reglas de negocio

| ID | Regla | Fuente |
|----|-------|--------|
| BR-001 | Un curso aportado entra al sistema en revisión y solo llega al catálogo comunitario tras validación | SPEC clase |
| BR-002 | Cada usuario ve y edita solo su propio roadmap | decisión propia |
| BR-003 | Quien aporta un curso declara si él/ella lo tomó | SPEC clase |
| BR-004 | Solo se permite la carga en catálogo de cursos 100% gratuitos que cuenten con un enlace web activo funcional | SPEC clase |
| BR-005 | No se permiten aportes duplicados que compartan el mismo enlace web de un curso ya existente | decisión propia |

## 8. Fuera de alcance (out of scope)

- **Cursos nativos y entrega de certificados**: La plataforma no ofrece cursos propios ni otorga certificados, su función es unicamente ofrecer enlaces a cursos externos.
- **Reproducción o alojamiento de contenido multimedia**: No se almacenan ni reproducen videos, audios o documentos dentro de la plataforma; únicamente se redirige mediante el enlace externo activo proporcionado.
- **Procesamiento de pagos o monetización**: La plataforma está orientada exclusivamente a cursos de acceso gratuito; no se integran pagos o suscripciones.
- **Integración automática con APIs externas**: No se sincroniza el progreso del usuario de forma automática con plataformas de terceros; el usuario es quien manualmente marca como completos sus avances en el curso.
- **Aplicación móvil nativa (iOS / Android)**: El producto es estrictamente una WebApp responsive diseñada bajo el enfoque **mobile-first**.
- **Interacción social avanzada**: No se incluyen foros de discusión, salas de chat en vivo, comentarios en tiempo real o sistemas de seguidores entre usuarios.

## 9. Supuestos y decisiones sobre la SPEC de clase

- **Moderación de aportes**: Se asume que los aportes de la comunidad se pueden gestionar manualmente por un usuario con rol Administrador a través de un panel porque permite un control más directo en la carga de potenciales enlaces dañinos o ajenos al ámbito educativo.
- **Privacidad del roadmap**: Se asume que el roadmap de cada usuario es un espacio privado e individual para ver su progreso; no hay necesidad que sea público.
- **Búsqueda de cursos**: Se asume que se puede aplicar filtros para agilizar la búsqueda.

Más detalle en [SPEC.md § 8](./SPEC.md#8-vacíos-de-la-spec-de-clase-y-decisiones-tomadas)

## 10. Preguntas abiertas

| Pregunta | Impacto | Estado |
|----------|---------|--------|
| ¿Los aportes expiran si nadie los valida? | bajo | Decidida: permanecen en cola de moderación sin expiración automática, al menos para la verisón MVP. |

---

**Referencias:**
- Atlassian — Plantilla PRD: https://www.atlassian.com/software/confluence/templates/product-requirements
- Lenny Rachitsky — Plantilla de requirements: https://www.atlassian.com/software/confluence/templates/requirements

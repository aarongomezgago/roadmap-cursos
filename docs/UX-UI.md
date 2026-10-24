# UX-UI — Guía visual de estilos — Learnity

## 1. Principios
1. **Mobile-first con mejora progresiva**: El layout base se diseña para 360px y se mejora, nunca se repara.
2. **Limpieza sobre adorno**: Se prioriza el espacio en blanco y la jerarquía tipográfica por encime de bordes pesados o cajas recargadas.
3. **Color con propósito de acción**: El azul primario de Google marca los elementos interactivos y llamadas a la acción.
4. **Estados defensivos son parte del diseño**: El estado de carga, vacío y de error se diseñan con la misma prioridad que la vista principal.
5. **Accesibilidad y objetivos no negociables**: Cualquier elemento interactivo cuenta con suficiente contraste, indicador de foco visible y una superficie de área de al menos 44px para dispositivos móviles.

## 2. Design tokens

### 2.1 Paleta de colores

| Token | Valor | Uso | Contraste AA |
|-------|-------|-----|--------------|
| `--color-primary` | `#1A73E8` | botones primarios, links | vs `--surface`: 4.5:1 ✓ |
| `--color-on-primary` | `#FFFFFF` | texto/iconos sobre primario | vs `--primary`: 4.5:1 ✓ |
| `--color-surface` | `#FFFFFF` | fondos de tarjetas | — |
| `--color-background` | `#F8F9FA` | fondo de página | — |
| `--color-text` | `#202124` | texto principal | vs `--background`: 15.27:1 ✓ |
| `--color-text-muted` | `#5F6368` | texto secundario | vs `--background`: 5.73:1 ✓ |
| `--color-success` | `#188038` | confirmaciones | — |
| `--color-warning` | `#F9AB00` | avisos | — |
| `--color-error` | `#D93025` | errores de validación | — |

### 2.2 Tipografía

| Token | Familia | Tamaño / line-height | Uso |
|-------|---------|----------------------|-----|
| `--font-family-base` | Roboto, system-ui, sans-serif | — | Cuerpo general |
| `--text-sm` | | 14px / 20px | metadatos |
| `--text-base` | | 16px / 24px | cuerpo |
| `--text-lg` | | 20px / 24px | títulos de sección |
| `--text-xl` | | 24px / 28px | títulos de página |

### 2.3 Espaciado, radios, sombras, z-index

| Token | Valor | Uso |
|-------|-------|-----|
| `--space-1` … `--space-8` | 4, 8, 12, 16, 24, 32, 40, 48 px | ritmo vertical (escala de 4px/8px), padding y gutters |
| `--radius-sm` | 8px | esquinas redoneadas para inputs, selects, badges |
| `--radius-md` | 12px | esquinas para tarjetas de cursos y contenedores |
| `--radius-lg` | 18px | Botones estilo pill (estética Material Design 3) y modales |
| `--shadow-sm` | 0 1px 2px rgba(60,64,67,.1), 0 1px 3px 1px rgba(60,64,67,.15) | elevación en reposo de tarjetas y header |
| `--shadow-md` | 0 1px 2px rgba(60,64,67,.1), 0 2px 6px 2px rgba(60,64,67,.15) | elevación, menu sandwich, modales |
| `--z-header` | 100 | posicionamiento de header superior |
| `--z-drawer` | 200 | posicionamiento del menu sandwich desplegable y overlay |
| `--z-toast` | 300 | posicionamiento superior para notificaciones |

### 2.4 Bloque de variables listo para copiar

```css
:root {
  --color-primary: #1A73E8;
  --color-on-primary: #FFFFFF;
  --color-surface: #FFFFFF;
  --color-background: #F8F9FA;
  --color-text: #202124;
  --color-text-muted: #5F6368;
  --color-success: #188038;
  --color-warning: #F9AB00;
  --color-error: #D93025;

  --font-family-base: "Roboto", system-ui, sans-serif;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.5rem;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 40px;
  --space-8: 48px;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radios-lg: 18px;

  --shadow-sm: 0 1px 2px rgba(60,64,67,.1), 0 1px 3px 1px rgba(60,64,67,.15);
  --shadow-md: 0 1px 2px rgba(60,64,67,.1), 0 2px 6px 2px rgba(60,64,67,.15);

  --z-header: 100;
  --z-drawer: 200;
  --z-toast: 300;
}
```

## 3. Estrategia mobile-first con mejora progresiva

| Capa | Dónde aplica | Qué define |
|------|--------------|------------|
| **Base (sin media queries)** | todos los viewports | layout de 1 columna, menú sándwich, tablas densas → cards apiladas, tipografía mobile, targets ≥ 44px |
| `@media (min-width: 768px)` | tablets | grilla de 2 columnas, navegación horizontal en el header, tablas como tabla real |
| `@media (min-width: 1024px)` | desktop | grilla de 3 columnas, contenedor principal centrado con max-width: 1140px, menu de navegación horizontal completo |

## 4. Componentes (anatomía + estados)

### 4.1 Botón (primario / secundario / peligro)

- Anatomía:
  - Primario: Fondo `--color-primary`, texto e icono `--color-on-primary`, radio `--radius-lg`, padding `10px 24px`, tipografía `--font-family-base` `--text-sm`
  - Secundario: Sin fondo, texto e icono `--color-primary`, radio `--radius-`, padding `10px 16px`
  - Peligro: `--color-error` sin fondo (requiere confirmación obligatoria antes de ejecutar)
- Estados: `default`, `hover`, `focus-visible`, `active`, `disabled`, `loading`

### 4.2 Campo de formulario (input / select)

- Anatomía:
  - Estilo Outlined, borde `1px solid --color-text-muted`, radio `--radius-sm`, padding `12px 16px`, label en `--color-text-muted` `--text-sm`, texto ingresado en `--color-text` `--text-base`
  - Mensajes de error con `aria-describedby`
- Estados: `default`, `focus`, `filled`, `error` (con mensaje asociado), `disabled`

### 4.3 Card de curso

- Anatomía:
  - Contenedor de superficie `--color-surface`, radio `--radius-md`, elevación reposo `--shadow-sm`, padding `--space-4`
  - Campos contenidos: Título del curso (`--text-lg --color-text`), chip de categoría (fondo `--color-background` con texto `--color-primary`), docentes (`--text-sm`, `--color-text-muted`) y badges de atributos (cuestionarios / examen / certificado / aval) con iconos Material Symbols
- Estados: `default`, `hover`, `seleccionada (en mi roadmap)`

### 4.4 Lista/tabla paginada

- Comportamiento por viewport:
  - Pantallas pequeñas (<768px): Las cards se apillan verticalmente para evitar scroll horizontal.
  - Tablets / desktop (>= 768px): Estructura de tabla tradiconal con divisores `--color-background`
- Paginación: Centrado horionalmente al pie del listado con botones de superficie 44x44px; la página actual destaca con `--color-primary` y texto `--color-on-primary`
- Estado vacío: Muestra componente Empty state

### 4.5 Menú sándwich

- Anatomía:
  - botón hamburguesa (icono `menu` Material Symbols) a la izquierda del header en viewports < 1024px
  - panel desplegable lateral izquierdo `width: 280px`, fondo `--color-surface`, elevacion `--shadow-md` y capa superior `--z-drawer` sobre overlay oscuro `rgba(32, 33, 34, 0)`
- Estados: cerrado, abierto
- Cierre: toque en link, botón X, tecla `ESC`, click fuera
- ARIA: `aria-expanded`, `aria-controls`, manejo de foco

### 4.6 Modal

- Anatomía:
  - Contenedor de superficie `--color-surface`, radio de bordes `--radius-lg`, sombra `--shadow-md`, centrado sobre overlay oscuro
  - Título `--text-xl`, cuerpo explicativo y barra de acción a la derecha (botón secundario "cancelar" + boton de confirmación)
- Estados: cerrado, abierto; con `focus trap`; cierre con `ESC`

### 4.7 Toast (notificación)

- Anatomía: Contenedor de superficie oscura `--color-text` con texto en `--color-surface`, radio `--radius-sm`, posición inferior y capa de elevación `--z-toast`.
- Tipos: éxito / error / info; duración automática de 4-6 segundos; `role="status"`

### 4.8 Skeleton y Empty state

- Skeleton: para `loading` de listados y detalle, bloques rectangulares de color `--color-background`
- Empty state: icono 48px en `--color-text-muted` + título `--text-lg --color-text` + mensaje + CTA ("Todavía no hay cursos en esta categoría — aportá el primero")

## 5. Layout y navegación

- **Header:**
  - Posicionamiento sticky en parte superior, superificie blanca `--color-surface`, incorpora sombra `--shadow-sm` al desplazar la página
  - En mobile: Extremo izquierdo con boton hamburguesa (menu sandwich) + Logo Learnity; Extremo derecho con icono de sesion.
  - En desktop: Boton hamburguesa oculto. Extremo izquierdo con logo Learnity. Centro y derecha con la barra de navegación horizontal completa (Catalogo / Aportar curso / Mi roadmap) y botones de sesion (Ingresar / Perfil)
- **Contenedores:** `max-width: 1140px`, centrado horizontalmente, padding lateral `--space-4` en moviles, `--space-5` en tablets / desktop.
- **Pantallas:**
> Detalle en [APPFlow.md](./APPFlow.md)
  - Catalogo comunitario (`/catalogo`): header superior sticky, barra de busqueda y filtros, grilla responsive de cards de curso y paginador centrado al pie.
  - Detalle de curso (`/catalogo/:id`): layout de 1 columna centrada con ficha del curso, metadatos, badges de atributos y boton primario "Agregar a mi roadmap".
  - Aportar curso (`/aportar`): formulario enfocado de 1 columna estructuradad en tarjetas de superficie `--color-surface` con campos estilo outlined.
  - Mi roadmap (`/roadmap`): vista organizada de cursos seleccionados por el usuario con indicadores de avance.
  - Autenticacion (`/login`, `/registro`): tarjeta centrada en pantalla sobre fondo `--color-background` con elevacion `--shadow-md` y foco directo en campos de credenciales.

## 6. Accesibilidad mínima (no negociable)

- [ ] Contraste AA (≥ 4.5:1) en todo texto; ≥ 3:1 en bordes de controles
- [ ] `:focus-visible` visible en todo elemento interactivo
- [ ] Menú sándwich con `aria-expanded` / `aria-controls` y foco gestionado
- [ ] `prefers-reduced-motion` respetado en transiciones
- [ ] Imágenes y iconos con `alt` o `aria-label`
- [ ] Errores de formulario asociados al campo (`aria-describedby`)

## 7. Iconografía y assets

- Set elegido: Material Symbols Outlined (Google Fonts)
- Por qué: Otorga integracion visual perfecta con la estética de Google fijada; vectores livianos en formato SVG/font.
- Tamaño y color por defecto de los iconos: Tamaño base de 24px × 24px (`1.5rem`), heredando el color del contenedor mediante `currentColor` (o `--color-text-muted` en elementos secundarios e inactivos).

---

**Referencias:**
- NN/g — Front-End Style-Guides (definición y checklist): https://www.nngroup.com/articles/front-end-style-guides/
- NN/g — Design Systems 101: https://www.nngroup.com/articles/design-systems-101/

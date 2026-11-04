# Changelog

## [v0.2.0] - 2026-11-03

### Added & changed (T1 - T11)
- Testing unitarios: funciones puras de negocio
- Testing de integracion con BD real
- Docker multi stage

### 📝 Retrospectiva
- El uso de ramas por ticket y conventional commits permitio mantener una historia limpia e integrable
- Se adapto la versión de PostgreSQL a 16-alpine por disponibilidad en los registros oficiales de Docker
- Se configuró el endpoint /health en Nginx
- Se limpiaron contenedores con metadata obsoleta para evitar inconsistencias en compose
- Stack 100% reproducible y verificado mediante tests y healthchecks

---

## [v0.1.0]- 2026-10-28

## Added
- Scaffold del proyecto: estructura backend/frontend, docker-compose de dev
- Backend mínimo: FastAPI con /health y GET /cursos
- Frontend mínimo: React + Vite consumiendo GET /cursos
# Manual de Laboratorio: Seguridad y Monitoreo en Git

Este repositorio contiene los ejemplos prácticos del manual de laboratorio sobre seguridad y monitoreo en Git. Aquí podrás encontrar configuraciones para proteger ramas, detectar secretos en tu código, integrar auditorías con Splunk, y limpiar el historial de Git.

## Ejercicios

1. **Configurar reglas de protección de ramas**
2. **Uso de Gitleaks para detectar secretos**
3. **Integrar auditoría con Splunk**
4. **Reparar un historial de Git con información sensible**

---

### Requisitos

- **Git**
- **Gitleaks**
- **Splunk**
- **GitHub Enterprise**

## Estructura

- **.git/**: Configuración de Git
- **.gitleaks.toml**: Configuración para Gitleaks
- **.gitignore**: Archivos que deben ser ignorados por Git
- **.env**: Ejemplo de archivo con secretos expuestos
- **config.env**: Archivo con información sensible que se elimina del historial de Git


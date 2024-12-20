# Laboratorio: Seguridad y Monitoreo de Git

Este repositorio demuestra prácticas seguras para la gestión y monitoreo de repositorios Git.

## Ejercicios
1. Configurar firmas GPG para commits seguros.
2. Implementar hooks de Git para reforzar políticas de seguridad.
3. Monitorear actividades en el repositorio con GitGuardian.
4. Auditar el historial del repositorio con BFG Repo-Cleaner.
5. Integrar registro y monitoreo con herramientas GitOps.

## Estructura
- **scripts/**: Contiene hooks personalizados de Git.
- **sensitive_data/**: Archivos de ejemplo con datos sensibles (para asegurar).
- **examples/**: Scripts de ejemplo para probar prácticas de seguridad.

---

Sigue los ejercicios en el manual del laboratorio para obtener pasos detallados.

## Cómo Usar Este Repositorio

1. Clona este repositorio:
   ```bash
   git clone https://github.com/<tu_usuario>/git-security-lab.git
Navega al directorio:

cd git-security-lab

chmod +x scripts/pre-commit
ln -s ../../scripts/pre-commit .git/hooks/pre-commit



Prueba los ejemplos:

Intenta hacer un commit con sensitive_data/secrets.txt incluido y observa cómo se bloquea.
Firma un commit utilizando secure_commit.txt.

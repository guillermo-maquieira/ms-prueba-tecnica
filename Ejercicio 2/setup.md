# Automatización de una web

Para ejecutar localmente la resolución del ejercicio se sugieren los siguientes pasos:

- Instalar [Python](https://python.org/) como lenguaje de programación y [pip](https://pip.pypa.io/en/stable/) como gestor de dependencias.
- Instalar [Virtualenv](https://virtualenv.pypa.io/en/latest/) para crear y posteriormente activar el entorno virtual donde instalar las dependencias.

Una vez verificados los pasos anteriores, ejecutar los siguientes comandos:

1. Crear un entorno virtual como carpeta oculta del proyecto:

```bash
python3 -m venv .venv
```

2. Activar el entorno virtual:

```bash
source .venv/bin/activate
```

3. Instalar [Selenium](https://pypi.org/project/selenium/) y [Webdriver-Manager](https://pypi.org/project/webdriver-manager/) por ser dependencias necesarias:

```bash
python3 -m pip install requirements.txt
```

4. Ejecutar el proyecto:

```bash
python3 automation.py
```
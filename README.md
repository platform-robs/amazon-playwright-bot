# Amazon Playwright Bot

## Prueba Técnica: Automatización de Compra en Amazon con Playwright

Este proyecto tiene como propósito **demostrar la automatización completa de un flujo de compra en Amazon México** utilizando **Playwright con Python**.

El bot simula la interacción de un usuario desde el inicio de sesión, la selección de una categoría, la elección de un producto y su adición al carrito, hasta visualizar la página de finalización de compra (sin ejecutar la compra real).

El proyecto permite su ejecución tanto en **modo headed (con interfaz visible)** como en **modo headless (sin interfaz gráfica)**, y expone una **API REST** para iniciar el flujo con credenciales y modo de ejecución dinámico.

---

## Objetivo

Desarrollar un proyecto funcional utilizando **Playwright**, en Python para automatizar un
proceso de compra de un producto específico en Amazon, desde la búsqueda hasta la
finalización del pedido. 

El proyecto deberá poder ejecutarse en modo **con interfaz (headed)** o **sin interfaz (headless)**.

---

## Características Principales

- Navegación automatizada en [amazon.com.mx](https://www.amazon.com.mx)
- Inicio de sesión con cuenta y contraseña recibidas por API
- Detecta si ya existe un inicio de sesión
- Selección automática de:
  - Categoría: *Electrónicos*
  - Subcategoría: *Televisión y video*
  - Filtro: *56" o más*
- Agrega el primer producto encontrado al carrito
- Simula el proceso de compra sin ejecutarlo
- Registro detallado de logs por sesión
- API REST para ejecutar el flujo dinámicamente
- Arquitectura modular con buenas prácticas

---

## Estructura del Proyecto

```
amazon-playwright-bot/
├── src/
│   ├── config.py
│   ├── locators.py
│   ├── logger.py
│   └── tests.txt
│
├── README.md
├── requirements.txt
└── setup_env
```

---
## Instalación y preparación del entorno

Este proyecto incluye un script (setup_env.py) que configura todo automáticamente: crea un entorno virtual e instala las dependencias necesarias.

**Requisitos previos:**

* Python 3.9 o superior
* Acceso a la terminal / línea de comandos
* pip actualizado (opcional pero recomendado):
* python -m pip install --upgrade pip

## Pasos para configurar el entorno

**Clonar el proyecto:**

`git clone https://github.com/platform-robs/amazon-playwright-bot.git`

**Ejecutar el script de configuración:**

`python setup_env.py`

**Esto hará automáticamente:**

1. Crear un entorno virtual en venv si no existe
2. Detectar el sistema operativo y usar el pip correcto
3. Instalar todas las dependencias de requirements.txt
4. Activar el entorno virtual (opcional para trabajar dentro del entorno):

**Windows:**

`venv\Scripts\activate`

**Linux / macOS:**

`source venv/bin/activate`

**Al finalizar correctamente debe mostrarse:**

`All done! The virtual environment is ready with all dependencies installed.`

**Activar el entorno virtual**

Antes de ejecutar cualquier script, activa el venv:

`.\venv\Scripts\Activate.ps1`

**Verificar versión de playwright**

`pip show playwright`

---

## Uso

Se deberan cambiar la contraseña y el correo del usuario; 
por el momento el cambio mediante endpoint se está trabajando en la rama **T-0001**

Durante la ejecución, se generará un archivo de log en el mismo directorio, con información de cada paso y cualquier error detectado.

Además de una carpeta con las capturas de pantalla para comprobar los detalles.

---

## Test

El bot se encuentra en el archivo *tests.py* 

Se puede correr directamente mediente la terminal, una vez que ya se haya activado el entorno virtual, utilizando el comando 

`python src\tests.py`

---

## Funcionalidades Principales

| Función | Descripción |
|----------|--------------|
| `run_test()` | <br>Ejecuta todo el flujo del bot: inicio de sesión, navegación, selección y compra simulada. <br><br>|
| `is_logged_in(page)` | <br>Verifica si ya existe una sesión activa en Amazon.<br><br> |
| `login(page)` | <br>Inicia sesión con las credenciales proporcionadas. <br><br>|
| `navigate_to_tvs(page)` | <br>Accede a la categoría de televisores y aplica el filtro de tamaño. <br><br>|
| `select_product(page)` | <br>Selecciona el primer producto disponible. <br><br>|
| `add_to_cart(page)` | <br>Agrega el producto al carrito. <br><br>|
| `proceed_to_checkout(page)` | <br>Abre el carrito y continúa hacia el proceso de compra. <br><br>|
| `logger` | <br>Registra todas las acciones y errores durante la ejecución. <br><br>|


---

## Seguridad y buenas prácticas

* No compartir credenciales reales en el repositorio.
* Ejecutar HEADLESS=True en entornos de producción o testing automatizado.
* Ejecutar HEADLESS=False mientras se realizan las pruebas locales.
* Los logs se almacenan en archivos separados para poder auditar los pasos del bot.



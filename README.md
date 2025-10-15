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
amazon-bot/
├── src/
│   ├── config.py
│   ├── locators.py
│   ├── logger.py
│   └── tests.txt
│
├── api/
│   └── api.py
│
├── requirements.txt
└── README.md
```

---
## Instalación

**1. Clonar el repositorio:**
```
git clone https://github.com/platform-robs/amazon-playwright-bot.git
cd amazon-playwright-bot/src
```

**2. Crear un entorno virtual (opcional pero recomendado):**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

*Para este caso, probando en Colab*
```
!pip install playwright

# Install browsers
!playwright install

import asyncio
import nest_asyncio

nest_asyncio.apply()

from playwright.async_api import async_playwright
```

**3. Instalar dependencias:**
```
pip install -r requirements.txt
```

**4. Instalar navegadores de Playwright:**
```
playwright install
```



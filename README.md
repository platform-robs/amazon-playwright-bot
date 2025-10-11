# Amazon Playwright Bot

## Prueba Técnica: Automatización de Compra en Amazon con Playwright

Este proyecto tiene como propósito **demostrar la automatización completa de un flujo de compra en Amazon México** utilizando **Playwright con Python**.
El bot simula la interacción de un usuario desde el inicio de sesión, la selección de una categoría, la elección de un producto y su adición al carrito, hasta visualizar la página de finalización de compra (sin ejecutar la compra real).

El proyecto permite su ejecución tanto en **modo headed (con interfaz visible)** como en **modo headless (sin interfaz gráfica)**, y expone una **API REST** para iniciar el flujo con credenciales y modo de ejecución dinámico.

---

## Objetivo

Desarrollar un proyecto funcional que automatice, mediante **Playwright**, el proceso de compra de un producto específico en Amazon.  
El flujo se ejecuta con credenciales proporcionadas vía API y puede correr en modo **con interfaz (headed)** o **sin interfaz (headless)**.

---

## Características Principales

- Navegación automatizada en [amazon.com.mx](https://www.amazon.com.mx)
- Inicio de sesión con cuenta y contraseña recibidas por API  
- Selección automática de:
  - Categoría: *Electrónicos*
  - Subcategoría: *Televisión y video*
  - Filtro: *Más de 55”*
- Agrega el primer producto encontrado al carrito  
- Simula el proceso de compra sin ejecutarlo  
- Registro detallado de logs por sesión  
- API REST para ejecutar el flujo dinámicamente  
- Arquitectura modular con buenas prácticas

---

## Estructura del Proyecto

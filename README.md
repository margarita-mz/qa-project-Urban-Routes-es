# Proyecto Urban Routes

Este proyecto corresponde al Sprint 9: "Automatización de pruebas de la aplicación web".

El objetivo del proyecto es automatizar pruebas para la aplicación Urban Routes, comprobando el flujo completo para pedir un taxi. Las pruebas validan acciones como configurar una ruta, seleccionar la tarifa Comfort, agregar un número de teléfono, agregar una tarjeta de crédito, escribir un mensaje para el conductor, pedir manta y pañuelos, pedir helados y confirmar que aparece el modal de búsqueda de taxi.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Google Chrome
- ChromeDriver
- Page Object Model, también conocido como POM

## Archivos principales del proyecto

- `data.py`: contiene los datos usados en las pruebas, como URL, direcciones, teléfono, tarjeta y mensaje para el conductor.
- `main.py`: contiene los localizadores, métodos de la página y las pruebas automatizadas.
- `.gitignore`: evita subir archivos innecesarios como el entorno virtual, caché de Python y archivos de PyCharm.

## Pruebas automatizadas

Las pruebas cubren el siguiente flujo:

1. Configurar la dirección de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Pedir manta y pañuelos.
7. Pedir dos helados.
8. Confirmar que aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor.

## Cómo ejecutar las pruebas

Primero, asegúrate de estar en la carpeta del proyecto:

```bash
cd qa-project-Urban-Routes-es
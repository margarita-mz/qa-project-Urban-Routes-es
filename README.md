# Proyecto Urban Routes

Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes.  
El objetivo es validar diferentes funcionalidades del flujo para pedir un taxi, utilizando Selenium WebDriver y pytest.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Google Chrome

## Estructura del proyecto

- `data.py`: contiene los datos de prueba utilizados en las pruebas.
- `helpers.py`: contiene la función para obtener el código de confirmación del teléfono.
- `pages.py`: contiene la clase `UrbanRoutesPage`, donde se encuentran los localizadores y métodos de interacción con la página.
- `main.py`: contiene la clase `TestUrbanRoutes` con los casos de prueba.
- `.gitignore`: evita subir archivos innecesarios al repositorio.

## Funcionalidades probadas

Las pruebas automatizadas validan los siguientes escenarios:

- Configurar la ruta de origen y destino.
- Seleccionar la tarifa Comfort.
- Rellenar el número de teléfono.
- Agregar una tarjeta de crédito.
- Ingresar el código de confirmación de la tarjeta.
- Escribir un mensaje para el conductor.
- Pedir una manta y pañuelos.
- Pedir dos helados.
- Confirmar que aparece el modal para buscar un taxi.
- Validar que aparece la información del conductor.



## Cómo ejecutar el proyecto

1. Clonar el repositorio:
`git clone URL_DEL_REPOSITORIO`
2. Entrar a la carpeta del proyecto:
`cd qa-project-Urban-Routes-es`
3. Instalar las dependencias necesarias:
`pip install selenium pytest`
4. Ejecutar las pruebas:
`pytest main.py`

### Resultado esperado

Al ejecutar las pruebas, todas deben pasar correctamente.

Ejemplo: `9 passed`


.
#### Notas:

Antes de ejecutar las pruebas, es importante verificar que la URL de Urban Routes en el archivo data.py esté actualizada y funcionando correctamente.

Solo cambia esta parte, por el link real de tu repositorio de GitHub cuando ya lo tengas:

```markdown
git clone URL_DEL_REPOSITORIO

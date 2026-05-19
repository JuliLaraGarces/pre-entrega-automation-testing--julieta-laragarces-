Pre-entrega Proyecto Final - Automatización de Testing

Propósito del Proyecto
El propósito de este proyecto es poder automatizar las siguientes pruebas de la página SauceDemo:

1 - Automatización de Login
    - Ingreso exitoso (contemplando contraseña y usuario correctos)
    - Ingreso no exitoso (cotemplando contraseña y usuario incorrectos, contraseña correcta y usuario incorrecto,
    contraseña incorrecta y usuario correcto, sin ingreso de credenciales (vacío))
2 - Navegación, verificación e interacción con el catálogo
    - Navegar por productos (Verificar que estén listados)
    - Acceder a detalle (Verificar que derivan al detalle correctamente)
    - Verificar que aparezcan los productos
3 - Interacción con productos
    - Añadir un producto (uno, varios)
    - Eliminar un producto
    - Navegar por el carrito

En todas las instancias se hace checkeo del título de la página y la redirección de la mísma en el bloque try.

Tecnologías Utilizadas
Python como lenguaje de programación, Pytest como Framework de testing para realizar las pruebas, Selenium para visualizar 
la automatización de la web y GitHub para respaldar el proyecto y realizar control de versiones.

Instalación de Dependencias
En el proyecto se utilizo Python, instalarlo desde la web oficial.
También se utilizó Selenium y Pytest, instalarlo con el siguiente comando en consola: pip install selenium pytest
Para la interfaz web: Selenium webdriver: https://googlechromelabs.github.io/chrome-for-testing/#stable el ChromeDriver
Instalar todo en el mismo path.

Comando para ejecutar las pruebas
Para ejecutar todas las pruebas: python -m pytest pre-entrega-automation-testing-julieta-laragarces/tests/test_saucedemo.py -v

Comando para generar reporte
Para generar un reporte HTML: python -m pytest pre-entrega-automation-testing-julieta-laragarces/tests/test_saucedemo.py -v --html=reporte.html

#Llamo a las librerías necesarias para la automatización con Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Primero preparo el entorno, instanciando el driver y configurando un tiempo de espera implícito
driver = webdriver.Chrome() #instancio el driver de Chrome
driver.implicitly_wait(5) #Tiempo de espera implícito para encontrar los elementos de la página

#Estas instancias no están moduladas en funciones (como por ejemplo la de login) o clases para mantener el código simple,
#pero en el proyecto final las voy a moduilarizar para que sea más ordenado y reutilizable.
#------------------------------------
#CASO DE USO: INTERACCIÓN CON EL CARRITO DE COMPRAS
#Caso de prueba 1: Seleccionar producto, agregar al carrito y verificar
#------------------------------------
try:
    # Abro la página de SauceDemo
    driver.get("https://www.saucedemo.com")

    # Completo con usuario y contraseña correctos, los busco por ID
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Busco el botón por Id (para mantener la buena práctica) y lo clickeo
    driver.find_element(By.ID, "login-button").click()
    
    #Verifico que se redirigió a la página de inventario y si no, caso contrario, se mostrará el mensaje de error
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    #Paralelamente, verifico que el título de la página sea el esperado, caso contrario, se mostrará un mensaje de error
    assert driver.title == "Swag Labs", "Título incorrecto"

    #Valido el título del header
    header_title = driver.find_element(
    #Busco el título de la sección
    By.CSS_SELECTOR, "div.header_secondary_container .title"
    ).text
    #Si coincide, se muestra que está en el módulo de productos, si no, está en otro lado
    assert header_title == "Products",f"No se encuentra en la página de inventario, está en: {header_title}"

    #Verifico que dentro de ese módulo, exista al menos un solo producto
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(productos) > 0, "No se encontraron productos"

    #Busco el nombre del producto
    producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item")

    #Guardo el nombre del producto en la variable nombre_producto
    nombre_producto  = producto.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    #Agrego al carrito
    producto.find_element(By.TAG_NAME, "button").click()   

    # Busco el contador del carrito y verifico que se actualizó a 1
    inventorio = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert inventorio == "1", f"Hay {inventorio} productos en el carrito"

    #Voy al ícono del carrito y lo clickeo
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    carrito = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
    assert carrito == nombre_producto, "No existe producto en el carrito o el producto es incorrecto"

    #Si las validaciones anteriores son correctas, se muestra el mensaje de éxito y el caso de prueba está aprobado
    print("TEST OK: SE AGREGÓ CORRECTAMENTE EL PRODUCTO AL CARRITO Y SE VERIFICÓ QUE ESTÁ.")
finally:
    #Cierro el navegador
    driver.quit()
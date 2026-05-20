#Llamo a las librerías necesarias para la automatización con Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Primero preparo el entorno, instanciando el driver y configurando un tiempo de espera implícito
driver = webdriver.Chrome() #instancio el driver de Chrome
driver.implicitly_wait(5) #Tiempo de espera implícito para encontrar los elementos de la página

#Estas instancias no están moduladas en funciones o clases para mantener el código simple,
#pero en el proyecto final las voy a moduilarizar para que sea más ordenado y reutilizable.
#------------------------------------
#CASO DE USO: LOGIN A LA PLATAFORMA
#Casos de prueba 1: Usuario y contraseña correctos
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

    #Si ambas validaciones anteriores son correctas, se muestra el mensaje de éxito y el caso de prueba está aprobado
    print("TEST OK: Login exitoso con usuario y contraseña correctos.")
finally:
    #Cierro el navegador
    driver.quit()


#------------------------------------
#CASO DE USO: LOGIN A LA PLATAFORMA
#Casos de prueba 2: Usuario y/o contraseña incorrectos
#------------------------------------
driver = webdriver.Chrome() #instancio el driver de Chrome
driver.implicitly_wait(5)
try:
    # Abro la página de SauceDemo
    driver.get("https://www.saucedemo.com")

    # Ingreso las credenciales incorrectas (en este caso la contraseña es incorrecta)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("password_incorrecto") 

    #Busco el botón por Id (para mantener la buena práctica) y lo clickeo
    driver.find_element(By.ID, "login-button").click()

    #Como la contraseña es incorrecta, se muestra el mensaje de error
    print("TEST OK: Login fallido con usuario y/o contraseña incorrectos.")

    #Paralelamente, verifico que no se redirigió a la página de inventario
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
finally:
    # 6) Cerrar el navegador
    driver.quit()

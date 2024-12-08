import os
from typing import List
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from GsiCharacter import GsiCharacter


'''
Jabes Rivas, 07.12.2024. Dangos.dev🍡. Proyecto [Hanami Dango]
Demostración de extracción de datos de personaje de Genshin Impact de un sitio web específico.
- Utiliza Selenium para automatizar acciones en el navegador
- Analiza el contenido completo de la página con BeautifulSoup
- Identifica e itera la tabla que contiene el contenido necesario
- Modela la información en una lista para su posterior uso

Como es una DEMOSTRACIÓN no se implementa:
- Algoritmos más refinados de identificación de elementos web
- Rutinas de manejo de errores
- Almacenamiento de los datos
- Expresiones con mejor rendimiento
'''


load_dotenv()

GSI_CHARACTERS_URL: str = os.getenv("GSI_CHARACTERS_URL") # Pregúntame por la URL
CHARACTERS_TABLEID: str = os.getenv("GSI_CHARACTERS_TABLE_ID") # Pregúntame por el ID
CHROME_DRIVER_PATH: str = r"resources\chromedriver.exe"
S_PAGINATION_XPATH: str = r'//*[@id="characters"]/table/tbody/tr/td[1]/select'

# Inicializa el servicio de Chrome para el Webdriver
chrome_service = Service(CHROME_DRIVER_PATH)

# Activa el flag para levantar chrome sin interfaz gráfica, //chrome --headless
# > https://developer.chrome.com/docs/chromium/headless
chrome_options = Options()
# chrome_options.add_argument('--headless=new')

# Inicializa el Webdriver y llama inmediatamente a la URL
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get(GSI_CHARACTERS_URL)

# La tabla de personajes muestra por defecto una paginación de 10 items/per page
# Con esto identificamos el selector y cambiamos a 100 items por página
pagination = Select(driver.find_element(By.XPATH, value = S_PAGINATION_XPATH))
pagination.select_by_visible_text("100")

# Teniendo ya la tabla mostrándose completa, descarga el HTML y lo analiza con BS4
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

# Identifica la tabla que contiene los personajes usando el id
# Existe otro algoritmo para detectar el cambio de id de la tabla. Mientras tanto, usa el del entorno
characters_table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == CHARACTERS_TABLEID )

# Analiza cada una de las líneas de la tabla y extrae la información, convirtiendola en el objeto deseado
character_list: List[GsiCharacter] = []

for row in characters_table.find_all('tr'): # Selecciona solo los elementos de línea de tabla [tr]
    # Con la línea cabecera se identifica en que index se encuentran los datos esperados
    if row.parent.name == 'thead':
        continue # Se omite la línea cabecera (demo)

    character_list.append(GsiCharacter.from_row(row))

print(character_list)
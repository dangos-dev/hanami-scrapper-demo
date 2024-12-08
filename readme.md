
# Hanami Dango🍡 - Web Scrapper Demo

Demostración de extracción de datos de personaje de Genshin Impact de un sitio web específico utilizando Selenium y BeautifulSoup.


## Instalación

Para instalar las dependencias necesarias en este proyecto se debe ejecutar primero:

```bash
  pip install -r requirements.txt
```

Pregúntame por los valores de variables de entorno ;)
## Características principales
- **Web Scraping**:
    - Utiliza Selenium para automatizar las interacciones del navegador web.
    - Carga la página web de destino (GSI_CHARACTERS_URL).
    - Ajusta la configuración de la página (paginación) para recuperar todos los datos de caracteres simulando la interacción de un usuario.
    - Descarga el contenido HTML completo de la página.

- **Análisis de datos**:
    - Emplea BeautifulSoup para analizar el contenido HTML.
    - Identifica y extrae la tabla relevante que contiene información de caracteres.
    - Recorre cada fila de la tabla.
    - Extrae atributos de caracteres específicos de cada fila.

- **Modelado de datos**:
    - Crea una clase GsiCharacter para representar y almacenar los datos de caracteres extraídos en un formato estructurado.
    - Llena una lista con instancias de la clase GsiCharacter, cada una de las cuales representa un solo personaje.

- **Salida**:
    - Imprime la lista de personajes en la consola y muestra los datos de caracteres extraídos.

Como es una DEMOSTRACIÓN no se implementa:
- Algoritmos más refinados de identificación de elementos web
- Rutinas de manejo de errores
- Almacenamiento de los datos
- Expresiones con mejor rendimiento
# M2.851 -TIPOLOGÍA Y CICLO DE VIDA DE LOS DATOS-
# Práctica 1: Web scraping

## Descripción

Este proyecto es el resultaado de la Práctica 1 de la asignatura _Tipología y ciclo de vida de los datos_, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya.<p>
La práctica se basa en obtener mediante técnicas de _web scraping_ codificadas bajo el lenguaje de programación Python datos de la web _bonarea.com_ y generar diferentes datasets acorde la elección del usuario. A su vez, se han generado diferentes aplicaciones de los datos obtenidos para mostrar ejemplos de la información que se podría extraer de los mismos.<p>
  
**Nota:**
El informe del proyecto se encuentra tanto en formato Rmd como HTML.<p>
Para visualizar el archivo HTML correctamente, se deberá descargar el archivo y **abrirlo con un navegador**.<p>


## Miembros del equipo

La actividad ha sido realizada por: **Olga Garcés Ciemerozum** y **Carlos Acosta Quintas**.

## Ficheros del código fuente

* **get_dataframe.py**: Generador de los diferentes dataframes 'a la carte' a petición del usuario (formato archivo: csv).
* **get_reports.py**: Generador de las diferentes aplicaciones 'a la carte' a petición del usuario (formato archivo: varios).
* **main_functions.py**: Contiene la implementación de las diferentes funciones para extraer los datos mediante técnicas de web scraping y la creación de los datasets.
* **plot_box.py**: Contiene la implementación de la aplicación para crear gráficos box plot con los datos extraídos.
* **plot_price_evolution.py**: Contiene la implementación de la aplicación para crear gráficos de evolución del precio según tipo de producto.
* **plot_heatmap.py**: Contiene la implementación de la aplicación para crear un heatmap geográfico de los precios según el producto escogido.


## Prerequesitos

Este projecto se ha implementado en Python 3.8.8. Se recomienda esta versión o posteriores para evitar incompatibilidades con el código fuente.<p>
El archivo requierements.txt muestra las librerías específicas que son requeridas para poder ejecutar correctamente el proyecto.<p>


## Instrucciones

Para poder ejecutar directamente este proyecto en tu máquina local, deberás clonar todo el repositorio mediante su dirección url.<p>
Una vez clonado, para generar los datasets, se debe ejecutar el archivo **get_dataframe.py** y seguir las instrucciones.<p>
El programa puede generar 2 tipos de datasets en formato csv:<p>

* Dataset en 2 ficheros csv: csv con los datos de las diferentes gasolineras (estático). y csv actualizable con los datos de los precios por producto diarios de las diferentes gasolineras.<p>
* Dataset completo en un fichero csv (combinación de los dos primeros datasets).<p>

Para ejecutar las aplicaciones existentes en el proyecto, se debe ejecutar **get_reports.py** y seguir las instrucciones.

El programa puede generar 4 tipos de gráficas:<p>

* Box plot por día de la semana con los estadísticos de los precios para una única gasolinera.<p>
* Box plot por día de la semana con los estadísticos de los precios de todas las gasolineras.<p>
* Gráfico de evolución temporal de los precios de cada producto y por gasolinera.<p>
* Heatmap geográfico de los precios por producto.<p>


## Recursos

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
3. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 5. Dynamic Data.  

## License

Database released under Open Data Commons Open Database License (ODbL) v1.0, individual contents under Database Contents License (DbCL) v1.0


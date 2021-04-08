# M2.851 -TIPOLOGÍA Y CICLO DE VIDA DE LOS DATOS-
# Práctica 1: Web scraping

## Descripción

Este proyecto es el resultado de la Práctica 1 de la asignatura _Tipología y ciclo de vida de los datos_, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya.<p>
La práctica se basa en obtener mediante técnicas de _web scraping_ codificadas bajo el lenguaje de programación Python datos de la web _bonarea.com_ y generar diferentes datasets acorde la elección del usuario. A su vez, se han generado diferentes aplicaciones de los datos obtenidos para mostrar ejemplos de la información que se podría extraer de los mismos.<p>
  
**Nota:**
El informe del proyecto se encuentra tanto en formato docx como en pdf.<p>

## Miembros del equipo

La actividad ha sido realizada por: **Olga Garcés Ciemerozum** y **Carlos Acosta Quintas**.

## Ficheros del código fuente 

* **get_dataframe.py**: Generador de los diferentes dataframes 'a la carte' a petición del usuario (formato archivo: csv).
* **get_reports.py**: Generador de las diferentes aplicaciones 'a la carte' a petición del usuario (formato archivo: varios).
* **main_functions.py**: Contiene la implementación de las diferentes funciones para extraer los datos mediante técnicas de web scraping y la creación de los datasets.
* **plot_box.py**: Contiene la implementación de la aplicación para crear gráficos box plot con los datos extraídos según carburante y día de la semana.
* **plot_price_evolution.py**: Contiene la implementación de la aplicación para crear gráficos de evolución del precio según tipo de carburante y gasolinera.
* **plot_heatmap.py**: Contiene la implementación de la aplicación para crear un heatmap geográfico de los precios según el carburante escogido.


## Prerequesitos

Este projecto se ha implementado en Python 3.8.8. Se recomienda esta versión o posteriores para evitar incompatibilidades con el código fuente.<p>
El archivo requierements.txt muestra las librerías específicas que son requeridas para poder ejecutar correctamente el proyecto.<p>
  
Para la elaboración de la visualización del heatmap, se deberá de disponer de una API de Google Maps. Se puede obtener una siguiendo las instrucciones en https://developers.google.com/maps.<p>


## Instrucciones

Para poder ejecutar directamente este proyecto en tu máquina local, deberás clonar todo el repositorio mediante su dirección url.<p>
Una vez clonado, para generar los datasets, se debe ejecutar el archivo "get_dataframe.py" y seguir las instrucciones.  

El proyecto puede generar 3 archivos con formato csv que formarán parte del dataset:

1.	Archivo csv “bonarea_gasolineras_prices.csv”: csv actualizable con histórico de precios diarios de los diferentes carburantes disponibles en las gasolineras.
2.	Archivo csv “bonarea_gasolineras_data_and_prices.csv”: csv actualizable con los datos informativos de las gasolineras e histórico de precios diarios de los diferentes carburantes disponibles.
3.	Archivo csv “bonarea_establecimientos.csv”: csv con la información descriptiva de todos los establecimientos de BonÀrea.



Para ejecutar las aplicaciones existentes en el proyecto, se debe ejecutar "get_reports.py" y seguir las instrucciones.

El programa puede generar 4 tipos de gráficas:<p>

* Box plot por día de la semana con los estadísticos de los precios para una única gasolinera.<p>
* Box plot por día de la semana con los estadísticos de los precios de todas las gasolineras.<p>
* Gráfico de evolución temporal de los precios de cada producto y por gasolinera.<p>
* Heatmap geográfico de los precios por producto.<p>



## Automatización de los datos

Debido a que parte del dataset se debe generar diariamente con los datos de referencia, si se desease automatizar el proceso, se debería crear, de forma local, una aplicación CRON en el sistema operativo (Linux / Mac) o gestionarlo mediante “Scheduled Tasks” de Windows. Dicho proceso sería útil si se mantuviese la máquina operativa 24 h, 7 días a la semana, con lo cual el usuario se podría despreocupar de ejecutar el archivo "get_dataframe.py" cada día.<p>


## Memoria

Este proyecto dispone de una memoria con información exhaustiva y explicaciones en cuanto a la elaboración del dataset. La memoria se dispone en formato docx y pdf en la carpeta "Informe".  

## License

Database released under Open Data Commons Open Database License (ODbL) v1.0, individual contents under Database Contents License (DbCL) v1.0

## Recursos

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
3. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 5. Dynamic Data.  

## Digital Object Identifier (DOI) del juego de datos
DOI: 10.5281/zenodo.4671856<p>
Link: https://doi.org/10.5281/zenodo.4671856
import requests
import json
import pandas as pd
import re
import copy
import csv
import os.path
import gmaps
from pandas.io.json import json_normalize
from datetime import datetime


from main_functions import build_request
from main_functions import get_response
from main_functions import get_data_by_id
from main_functions import get_id_by_entityType
from main_functions import get_df_row_by_id
from main_functions import update_dataframe
from plot_box import box_price_one_id
from plot_box import box_price_all_id
from plot_heatmap import heatmap
from plot_price_evolution_by_id import evolucion_precio_gasolinera



# Argumentos de las funciones para obtener los informes
csv_file = 'bonarea_gasolineras_prices.csv'
product_list = ["GASOIL A", "GASOLINA S/P 95", "GASOLINA S/P 98", "ADBLUE"]
type_options = ["1","2","3","4"]

# API usada para realizar la práctica
# api = "AIzaSyDAQtZoSJcyMCoLMBIutENA3WrMLf3YF3w"

api = "AIzaSyDAQtZoSJcyMCoLMBIutENA3WrMLf3YF3w"

# Inicialización id gasolinera
petrol_station_id = "A"

print("Following reports are currently available: ")
print()
print("Type of report = 1 -> Box Plot for one selected Id")
print("Type of report = 2 -> Box Plot for all Id")
print("Type of report = 3 -> Line Plot showing price evolution for one selected Id")
print("Type of report = 4 -> Geographical HeatMap with the prices by product of all petrol stations: ")
print()

select_report = str(input("Enter type of report you want to create: 1, 2, 3 o 4"))

if select_report == "4":
    pass
else:
    print()
    print()
    print("These are the available Petrol Station Id: ")
    print()
    print()
    print(get_id_by_entityType())
    petrol_station_id = str(input("Enter the petrol station Id:")).upper()

print()
print()
print("Following petrol products are currently available: ")
print()
print("Product Types:")
print("  -> GASOIL A")
print("  -> GASOLINA S/P 95")
print("  -> GASOLINA S/P 98")
print("  -> ADBLUE")
print()

petrol_product_type = str(input("Enter the petrol product(GASOIL A, GASOLINA S/P 95, GASOLINA S/P 98 o ADBLUE):")).upper()


def report(type_report):
    if petrol_station_id not in get_id_by_entityType():
        result = print("Please, introduce correct Petrol Station Id!")
    
    elif petrol_product_type not in product_list:
        result = print("Please, introduce correct Petrol product!")

    elif select_report not in type_options:
        result = print("Please, introduce correct type of report!")    
    
    else:
        if (type_report == "1"):
            #Report 1
            result = box_price_one_id(csv_file,
                                      petrol_station_id,
                                      petrol_product_type)

        elif (type_report == "2"):
            # Report 2
            result = box_price_all_id(csv_file,
                                      petrol_product_type)

        elif (type_report == "3"):
            # Report 3
            result = evolucion_precio_gasolinera(csv_file ,
                                                 petrol_station_id,
                                                 petrol_product_type)

        elif (type_report == "4"):
            # Report 4
            result = heatmap(api, csv_file, petrol_product_type)


    return result

report(select_report)
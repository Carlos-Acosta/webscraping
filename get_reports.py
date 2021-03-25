import requests
import json
import pandas as pd
import re
import copy
import csv
import os.path
from pandas.io.json import json_normalize
from datetime import datetime


from main_functions import build_request
from main_functions import get_response
from main_functions import get_by_id
from main_functions import get_id_gasolineras
from main_functions import get_df_row_by_id
from main_functions import update_dataframe
from plot_box import box_price_one_id
from plot_box import box_price_all_id
from plot_price_evolution_by_id import evolucion_precio_gasolinera

csv_file = "bonarea_gasolineras.csv"
product_list = ["GASOIL A", "GASOLINA S/P 95", "GASOLINA S/P 98", "ADBLUE"]
type_options = ["1","2","3"]



print(get_id_gasolineras())
petrol_station_id = str(input("Enter the petrol station Id:"))

print()
print("Product Types:")
print("  GASOIL A")
print("  GASOLINA S/P 95")
print("  GASOLINA S/P 98")
print("  ADBLUE")
print()

petrol_product_type = str(input("Enter the petrol product(GASOIL A, GASOLINA S/P 95, GASOLINA S/P 98 o ADBLUE):"))

print()
print("Type of report = 1 -> Box Plot for one selected Id")
print("Type of report = 2 -> Box Plot for all Id")
print("Type of report = 3 -> Line Plot showing price evolution for one selected Id")
print()

select_report = str(input("Enter type of report: 1, 2 o 3"))



def report(type_report):
    if petrol_station_id not in get_id_gasolineras():
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

    return result

report(select_report)
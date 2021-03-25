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
from box_plot import box_price_one_id
from box_plot import box_price_all_id
from price_evolution_by_id import evolucion_precio_gasolinera

csv_file = "bonarea_gasolineras.csv"


petrol_station_id = input("Enter the petrol station Id:")
petrol_product_type = input("Enter the petrol product(GASOIL A, GASOLINA S/P 95, GASOLINA S/P 98 o ADBLUE):")

#Elaborar más las descripciones......


def report():
    select_report = input("Enter type of report: 1, 2 o 3")
    if select_report == 1:
        #Report 1
        return box_price_one_id(csv_file , petrol_station_id, petrol_product_type)

    elif select_report == 2:
        # Report 2
        return box_price_all_id(csv_file , petrol_product_type)

    elif select_report == 3:
        # Report 3
        return evolucion_precio_gasolinera(csv_file ,
                                petrol_station_id,
                                petrol_product_type)

report()
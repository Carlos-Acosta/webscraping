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
from main_functions import get_data_by_id
from main_functions import get_id_by_entityType
from main_functions import get_df_row_by_id
from main_functions import update_dataframe
from main_functions import update_prices
from main_functions import update_data_and_prices
from main_functions import update_dataframe


type_options = ["1","2","3"]

print("In order to optimize memory and storage, there are several options to get bonarea dataframe.")
print()
print()
print("  -> Option 1: One dataset with only petrol station identification and description data")
print("  -> Option 2: One dataset with only variable data related with petrol product prices")
print("  -> Option 3: One full dataset with all data (petrol station constant and variable data")
print()
print()
print("Option 1 will get a static dataset of the petrol station with constant data like address, city, associated services, etc.")
print("This option is useful if you wish description data about the petrol station")
print()
print()
print("Option 2 will get a updated dataset of the petrol station prices by product every time the query is risen")
print()
print()
print("Option 3 will get the combination of option 1 and 2 (easier to handle, but it is not optimized for memory purposes)")


type_of_dataset = str(input("Enter the selected option: "))


def dataframe(type_of_dataset):
    if type_of_dataset not in type_options:
        dataframe = print("Please, introduce correct type of dataset!")    
    
    else:
        if (type_of_dataset == "1"):
            #Dataframe 1
            dataframe = update_dataframe("benzinera")
            #dataframe = update_dataframe_combinado("benzinera", "box", "bufet")

        elif (type_of_dataset == "2"):
            # Dataframe 2
            dataframe = update_prices("benzinera")

        elif (type_of_dataset == "3"):
            # Dataframe 3
            dataframe = update_data_and_prices("benzinera")
        
    return dataframe


dataframe(type_of_dataset)







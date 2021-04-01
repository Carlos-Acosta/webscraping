import requests
import json
import pandas as pd
import re
import copy
import csv
import os.path
from pandas.io.json import json_normalize
from datetime import datetime


def build_request(list_of_types = ["benzinera"]):
    """[summary]
        build_request generates a json search string from parameters
    Args:
        list_of_types (list, optional): [a list of entity types]. Defaults to ["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"].

    Returns:
        [str]: [string to be used put a request to a webpace]
    """
    res = "options["+str(list_of_types[0])+"]=true&"
    
    for types in list_of_types[1:len(list_of_types)]:    
        res += "options["+types+"]=true&"

    res += "language=ca"

    return res


# def get_response(request_str):
#     """[summary]
#         Uses a search string to place a post request. Returns the response formatted as json
#     Args:
#         request_str ([str]): [a search string that contains the parameters necessary to place a post request]
#     """

#     data = request_str
#     headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#                'origin': 'https://www.bonarea.com',
#                'Referer': 'https://www.bonarea.com/ca/default/locate'}

#     url = 'https://www.bonarea-agrupa.com/locator/Localitzador/Get'
#     response = requests.post(url, data=data, headers=headers)
#     resp = response.json()
#     return resp


def get_response1(entity_type="benzinera"):
    """[summary]
        Uses a search string to place a post request. Returns the response formatted as json
    Args:
        request_str ([str]): [a search string that contains the parameters necessary to place a post request]
    """

    data = build_request([entity_type])
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'origin': 'https://www.bonarea.com',
               'Referer': 'https://www.bonarea.com/ca/default/locate'}

    url = 'https://www.bonarea-agrupa.com/locator/Localitzador/Get'
    response = requests.post(url, data=data, headers=headers)
    resp = response.json()
    return resp

# def get_id_by_entityType(entity_type="benzinera"):
#     """
#     uses the response from get_response and extracts data such as id, coordenades, type, etc. 
#     not all data types can be extracted from this view. So we return a list of ids and iterate over them later. 
#     """
#     response = get_response(build_request([entity_type]))
#     ids = []
#     for data in response:
#         id = data["id"]
#         ids.append(id)

    return ids

def get_id_by_entityType1(entity_type="benzinera"):
    """
    uses the response from get_response and extracts data such as id, coordenades, type, etc. 
    not all data types can be extracted from this view. So we return a list of ids and iterate over them later. 
    """
    response = get_response1(entity_type)
    ids = []
    for data in response:
        id = data["id"]
        ids.append(id)

    return (ids, entity_type)



# def get_data_by_id(id):
#     """
#     gets a response for all relevant information belonging to an id. At this point the function just sends a request to the ajax page
#     and gets back a json code
#     """
#     headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#             'origin': 'https://www.bonarea.com',
#             'Referer': 'https://www.bonarea.com/ca/default/locate'}
#     url = 'https://www.bonarea-agrupa.com/locator/Localitzador/GetByID'
#     data = "id="+id+"&tipus=BENZINERA&language=ca"
#     response = requests.post(url, data=data, headers=headers)
#     resp = response.json()
#     return resp

def get_data_by_id1(id, entity_type="benzinera"):
    """
    gets a response for all relevant information belonging to an id. At this point the function just sends a request to the ajax page
    and gets back a json code
    """
    
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bonarea.com',
            'Referer': 'https://www.bonarea.com/ca/default/locate'}
    url = 'https://www.bonarea-agrupa.com/locator/Localitzador/GetByID'
    data = "id="+str(id)+"&tipus="+entity_type+"&language=ca"
    response = requests.post(url, data=data, headers=headers)
    resp = response.json()
    return resp



def get_df_row_by_id(gasolinera_id, entity_type="benzinera"):
    """gets a non-nested dafaframe of one row with all related petrol station values"""
    #check here
    dicc = get_data_by_id1(gasolinera_id, entity_type)
    df_dicc = pd.DataFrame([dicc])

    df_dicc["Fecha"] = datetime.today().strftime('%d-%m-%Y')
    df_dicc["Dia_Semana"] = (datetime.today().weekday() + 1)
    list_type = [1, 2, 3, 4, 5, 6, 7]
    list_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df_dicc["Dia_Semana"] = df_dicc["Dia_Semana"].replace(list_type, list_dias)

    df_dicc_address = pd.json_normalize(df_dicc["address"])
    df_dicc_coordenades = pd.json_normalize(df_dicc["coordenades"])

    column_names_preus = ["GASOIL A", "GASOLINA S/P 95", "GASOLINA S/P 98", "ADBLUE"]
    df_preus = pd.DataFrame(columns = column_names_preus)

    for i in  df_dicc["preus"][0]:
        for j in column_names_preus:
            if j in i:
                if i[-3] == ",":
                    df_preus.at[0, j] = int(i[-5:].replace(',', '')+"0")/1000
                else:
                    df_preus.at[0, j] = int(i[-5:].replace(',', ''))/1000

    column_names_serveis = ['RENTADOR', 'CANVI', 'SUPER', 'LAVABO', 'PARKING', 'VENDING']
    df_serveis = pd.DataFrame(columns = column_names_serveis)

    for i in  df_dicc["serveis"][0]:
        for j in column_names_serveis:
            if j in i:
                df_serveis.at[0, j] = 1

    result = pd.concat([df_dicc[["id", "type", "url"]],
                        df_dicc_address[["street", "city", "postalCode", "raoSocial"]],
                        df_dicc_coordenades,
                        df_serveis],
                        axis=1)

    result_preus = pd.concat([df_dicc[["id", "Fecha", "Dia_Semana"]],
                              df_dicc_coordenades,
                              df_preus],
                              axis=1)


    result_all = pd.concat([df_dicc[["id", "Fecha", "Dia_Semana", "type", "url"]],
                            df_dicc_address[["street", "city", "postalCode", "raoSocial"]],
                            df_dicc_coordenades,
                            df_serveis,
                            df_preus],
                            axis=1)

    return (result, result_preus, result_all)



# YA NO SE UTILIZA

# def update_dataframe(entity_type = "benzinera"):
#     """Creates dataframe if csv file does not exist and 
#     updates existing dataframes with new data
#     """

#     # eliminar el 1 del nombre del csv
#     id_gasolineras_list = get_id_by_entityType(entity_type)
#     csv_name = 'bonarea_gasolineras.csv'
#     if os.path.isfile(csv_name):
#         pass
#     else:
#         with open(csv_name,'a', newline='') as csvfile:
#             csvfile.write(get_df_row_by_id(id_gasolineras_list[0])[0].to_csv(index=False, header=True))
#             for i in range(1,len(id_gasolineras_list)):
#                 csvfile.write(get_df_row_by_id(id_gasolineras_list[i])[0].to_csv(index=False, header=False))
        
#     return


def update_prices(entity_type = "benzinera"):
    """Creates dataframe with prices of fuel
    """
    id_gasolineras_list = get_id_by_entityType1(entity_type)[0]
    csv_name = 'bonarea_gasolineras_prices.csv'
    if os.path.isfile(csv_name):
        with open(csv_name,'a', newline='') as csvfile:
            for i in range(0,len(id_gasolineras_list)):
                csvfile.write(get_df_row_by_id(id_gasolineras_list[i])[1].to_csv(index=False, header=False))
    else:
        with open(csv_name,'a', newline='') as csvfile:
            csvfile.write(get_df_row_by_id(id_gasolineras_list[0])[1].to_csv(index=False, header=True))
            for i in range(1,len(id_gasolineras_list)):
                csvfile.write(get_df_row_by_id(id_gasolineras_list[i])[1].to_csv(index=False, header=False))
    return


def update_data_and_prices(entity_type = "benzinera"):
    """Creates dataframe with prices of fuel
    """
    id_gasolineras_list = get_id_by_entityType1(entity_type)[0]
    csv_name = 'bonarea_gasolineras_data_and_prices.csv'
    if os.path.isfile(csv_name):
        with open(csv_name,'a', newline='') as csvfile:
            for i in range(0,len(id_gasolineras_list)):
                csvfile.write(get_df_row_by_id(id_gasolineras_list[i])[2].to_csv(index=False, header=False))
    else:
        with open(csv_name,'a', newline='') as csvfile:
            csvfile.write(get_df_row_by_id(id_gasolineras_list[0])[2].to_csv(index=False, header=True))
            for i in range(1,len(id_gasolineras_list)):
                csvfile.write(get_df_row_by_id(id_gasolineras_list[i])[2].to_csv(index=False, header=False))
    return
    
def update_dataframe_entity(out_file, entity_type):
    """Creates dataframe if csv file does not exist and 
    updates existing dataframes with new data
    """
    id_establecimientos_list = get_id_by_entityType1(entity_type)
    csv_name = out_file
    if os.path.isfile(csv_name):
        with open(csv_name,'a', newline='') as csvfile:
            for i in range(0,len(id_establecimientos_list[0])):
                csvfile.write(get_df_row_by_id(id_establecimientos_list[0][i], entity_type)[0].to_csv(index=False, header=False))
    else:
        with open(csv_name,'a', newline='') as csvfile:
            fields = list(get_df_row_by_id(id_establecimientos_list[0], entity_type)[0].columns)
            write_ = csv.writer(csvfile)
            write_.writerow(fields)
            for i in range(0,len(id_establecimientos_list[0])):
                csvfile.write(get_df_row_by_id(id_establecimientos_list[0][i], entity_type)[0].to_csv(index=False, header=False))
        
    return

def update_dataframe_global():
    out_file = "bonarea_establecimientos.csv"
    entidades = ["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"]
    if os.path.isfile(out_file):
        pass
    else:
        for i in entidades:
            update_dataframe_entity(out_file, i)
        



def update_dataframe1(out_file, entity_type = "benzinera"):
    """Creates dataframe if csv file does not exist and 
    updates existing dataframes with new data
    """

    # eliminar el 1 del nombre del csv
    id_gasolineras_list = get_id_by_entityType1(entity_type)
    csv_name = out_file
    if os.path.isfile(csv_name):
        pass
    else:
        with open(csv_name,'a', newline='') as csvfile:
            csvfile.write(get_df_row_by_id(id_gasolineras_list[0], entity_type)[0].to_csv(index=False, header=True))
            for i in range(1,len(id_gasolineras_list)):
                csvfile.write(get_df_row_by_id(id_gasolineras_list[i], entity_type)[0].to_csv(index=False, header=False))
        
    return



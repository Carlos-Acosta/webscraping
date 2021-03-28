from main_functions import build_request, get_response, get_data_by_id, get_id_by_entityType, get_df_row_by_id, get_data_by_id

from main_functions import update_prices, update_data_and_prices, update_dataframe
import pandas as pd
r = get_response("options[super]=true&options[botiga]=true&options[benzinera]=true&options[bufet]=true&options[box]=true&options[cash]=true&options[deposit]=true&language=ca")


#build_request(list_of_types = ["super", "botiga", "benzinera", "bufet", "box", "cash", "deposit"])

#get_data_by_id("A")



#print(list(map(get_data_by_id, get_id_by_entityType())))

#print(get_id_by_entityType("benzinera"))



#print(get_df_row_by_id("A")[1])
#print(get_df_row_by_id("A"))

#update_dataframe1("benzinera")

update_prices("benzinera")

update_data_and_prices("benzinera")

update_dataframe("benzinera")
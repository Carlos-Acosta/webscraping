from main_functions import build_request, get_response, get_data_by_id, get_id_by_entityType, get_df_row_by_id, get_object_data, get_data_by_id

from main_functions import update_dataframe1, get_df_row_by_id1, update_prices
import pandas as pd
r = get_response("options[super]=true&options[botiga]=true&options[benzinera]=true&options[bufet]=true&options[box]=true&options[cash]=true&options[deposit]=true&language=ca")


#build_request(list_of_types = ["super", "botiga", "benzinera", "bufet", "box", "cash", "deposit"])

#get_data_by_id("A")



#print(list(map(get_data_by_id, get_id_by_entityType())))

#print(get_id_by_entityType("benzinera"))



#print(get_df_row_by_id1("A")[1])
print(get_df_row_by_id1("A"))

update_dataframe1("benzinera")

update_prices("benzinera")
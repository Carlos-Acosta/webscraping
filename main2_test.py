from main_functions1 import build_request, get_response, get_id_by_entityType, get_data_by_id, update_prices, update_dataframe, get_df_row_by_id, update_data_and_prices
import pandas as pd
import time

print("\n\n Request1 \n\n")
print(build_request(["benzinera"]))
print("\n\n Request2 \n\n")
print(build_request(["cash", "diposit"]))

print("\n\n Response1 \n\n")
print(get_response(entity_type=["benzinera"]))
print("\n\n Response2 \n\n")
print(get_response(entity_type=["cash", "diposit"]))

print("\n\n GetData by entity Type1 \n\n")
print(get_id_by_entityType(entity_type=["benzinera"]))

print("\n\n GetData by entity Type 2 \n\n")
print(get_id_by_entityType(entity_type=["cash", "diposit"]))

print("\n\n GetData by Id 1 \n\n")
print(get_data_by_id("99236", entity_type="DIPOSIT"))

print("\n\n GetData by Id 1 \n\n")
print(get_data_by_id("791", entity_type="cash"))

print("\n\n Get Df row by id 1 \n\n")
print(get_df_row_by_id("99236", entity_type="DIPOSIT"))

print("\n\n Get Df row by id 2 \n\n")
print(get_df_row_by_id("791", entity_type="cash"))




s = time.time()   
print(s)
update_dataframe(["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"])
e = time.time()
print(e)
print(e-s)
from try_selenium import *

for line in get_all_data_by_id():
    id = line["id"]
    prices = line["preus"]
    for price in prices:
        if price.startswith("GASOIL A"):
            print(price)
from main_functions import get_response1, get_data_by_id1, update_dataframe1, build_request, get_id_by_entityType1, get_df_row_by_id


# datos por id, en función del id y tipo de intidad
#print(get_data_by_id1("42376", "BOTIGA"))


# actualiza dataframe con el nmbre del csv y el tipo de entidad - comprueba bot, box, buf csv
update_dataframe1("ben1.csv", "benzinera")
update_dataframe1("box1.csv", "box")
update_dataframe1("bu1f.csv", "bufet")




# tu función con poco cambio, le metes id, devuelve línea
# NOTA: hay que pasarle el tipo de entidad, sino por defecto es benzinera

#print("\n\n\n formato incorrecto \n\n\n")
#print(get_df_row_by_id(42305)) # no funciona

##print("\n\n\n formato correcto \n\n\n")
#print(get_df_row_by_id("42305", "botiga")) # funciona




#print("\n\n\n datos de una tienda \n\n\n")
#print(get_data_by_id1(id="42305", entity_type="botiga"))

#print("\n\n\n todos los ids de tiendas \n\n\n")
#print(get_id_by_entityType1(entity_type="botiga"))

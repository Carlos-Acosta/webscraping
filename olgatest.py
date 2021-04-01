from main_functions import  update_dataframe_entity, update_dataframe_global
from functions1 import update_dataframe
import time

# datos por id, en función del id y tipo de intidad
#print(get_data_by_id1("42376", "BOTIGA"))

# actualiza dataframe con el nmbre del csv y el tipo de entidad - comprueba bot, box, buf csv
#update_dataframe2("ben1.csv", "bufet")
#update_dataframe1("box1.csv", "box")
#update_dataframe1("bu1f.csv", "bufet")
#print(get_df_row_by_id(id_gasolineras_list[0], entity_type))
start = time.time()
update_dataframe_global()
end = time.time()
durationC = end - start
print("Carlos ", durationC)

start = time.time()
update_dataframe(["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"])
end = time.time()
durationO = end - start
print("Olga ", durationO)

print("and the winner is:")
print(min(durationC, durationO))

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

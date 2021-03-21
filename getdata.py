from try_selenium import get_all_data_by_id
from try_selenium import get_by_id,get_data
from try_selenium import get_object_data
from try_selenium import get_response
import pandas as pd

print(type(get_by_id("G058")))

df = pd.DataFrame.from_dict(get_by_id("G058"), orient="index")
df


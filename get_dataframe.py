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



#update_dataframe(get_id_by_entityType("benzinera"))

update_prices("benzinera")

update_data_and_prices("benzinera")

update_dataframe("benzinera")

# test
# test 2

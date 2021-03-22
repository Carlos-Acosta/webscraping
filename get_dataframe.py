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
from main_functions import get_by_id
from main_functions import get_id_gasolineras
from main_functions import get_df_row_by_id
from main_functions import update_dataframe


list_petrol_station = get_id_gasolineras()

update_dataframe(list_petrol_station)
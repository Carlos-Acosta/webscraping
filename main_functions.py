import requests
import json

"""driver = webdriver.Chrome(executable_path='/Users/olgagarcesciemerozum/chromedriver')
driver.get("https://www.bonarea.com/ca/default/locate")
print("learning to work with github")
print("")
place = driver.find_element_by_xpath('//*[@id="lblBotiga"]')
place.click()"""


def build_request(list_of_types = ["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"]):
    """[summary]
        build_request generates a json search string from parameters
    Args:
        list_of_types (list, optional): [a list of entity types]. Defaults to ["super", "botiga", "benzinera", "bufet", "box", "cash", "diposit"].

    Returns:
        [str]: [string to be used put a request to a webpace]
    """
    res = "options["+list_of_types[0]+"]=true&"
    
    if len(list_of_types) == 1:
        res = "options["+list_of_types[0]+"]=true&language=ca"

    for types in list_of_types[1:len(list_of_types)]:    
        res += "options["+types+"]=true&"
    
    res += "language=ca"
    return res


def get_response(request_str):
    """[summary]
        Uses a search string to place a post request. Returns the response formatted as json
    Args:
        request_str ([str]): [a search string that contains the parameters necessary to place a post request]
    """

    data = request_str
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'origin': 'https://www.bonarea.com',
               'Referer': 'https://www.bonarea.com/ca/default/locate'}

    url = 'https://www.bonarea-agrupa.com/locator/Localitzador/Get'

    #params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
    response = requests.post(url, data=data, headers=headers)
    resp = response.json()
    print(resp)

#get_response(build_request())


def get_data():
    """
    uses the response from get_response and extracts data such as id, coordenades, type, etc. 
    not all data types can be extracted from this view. So we return a list of ids and iterate over them later. 
    """
    ids = []
    for line in get_response(build_request()):
        id = line["id"]
        line["type"]
        #line["phone"]
        #line["phone2"]
        line["coordenades"]["latitude"]
        line["coordenades"]["longitude"]
        line["address"]["street"]
        line["address"]["number"]
        line["address"]["city"]
        line["address"]["province"]
        line["closest"]
        ids.append(id)

    return ids



def get_by_id(id):
    """
    gets a response for all relevant information belonging to an id. At this point the function just sends a request to the ajax page
    and gets back a json code
    """
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bonarea.com',
            'Referer': 'https://www.bonarea.com/ca/default/locate'}
    url = 'https://www.bonarea-agrupa.com/locator/Localitzador/GetByID'
    data = "id="+id+"&tipus=BENZINERA&language=ca"
    #params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
    response = requests.post(url, data=data, headers=headers)
    resp = response.json()
    return resp

#get_by_id("A")


# def get_all_data_by_id():
#     """
#     Maps the function get_by_id to the list of ids obtained from get_data()
#     The result is a list of json codes that help identifying different fields
#     """
#     return list(map(get_by_id, get_data()))
  
# def get_object_data():
#     """
#     uses the return from get_all_data_by_id, extracts the fields from each item of the list.
#     note: prices are a list too, they will need to be worked on with regex or something similar
#     """
#     for line in get_all_data_by_id():
#         id = line["id"]
#         types = line["type"] 
#         street = line["address"]["street"]
#         num = line["address"]["number"]
#         city = line["address"]["city"]
#         phone = line["address"]["phone"]
#         postcode = line["address"]["postalCode"]
#         sa = line["address"]["raoSocial"]
#         hours = line["horari"]
#         lat = line["coordenades"]["latitude"]
#         lon = line["coordenades"]["longitude"]
#         closest = line["closest"]
#         prices = line["preus"]
#         services = line["serveis"]
#         print(prices)



#"""again use get all data by id, here we´re interested only in the price of different types of fuel
#In the following code I´m attempting.. and getting the prices of gasoil A. This will have to be split into key - value pairs 
#as in a dictionary or maybe saved as csv. From here we can go on and do a scheduled scraping
"""
# for line in get_all_data_by_id():
#     id = line["id"]
#     prices = line["preus"]
#     for price in prices:
#         if price.startswith("GASOIL A"):
#             print(price)


#get_by_id("G027")

    



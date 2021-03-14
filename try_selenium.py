import requests
import json

"""driver = webdriver.Chrome(executable_path='/Users/olgagarcesciemerozum/chromedriver')
driver.get("https://www.bonarea.com/ca/default/locate")
print("learning to work with github")
print("")
place = driver.find_element_by_xpath('//*[@id="lblBotiga"]')
place.click()"""


def get_response(): 
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.bonarea.com', 'Referer': 'https://www.bonarea.com/ca/default/locate'}
    url = 'https://www.bonarea-agrupa.com/locator/Localitzador/Get'
    data = 'options[botiga]=true&options[super]=true&language=es'
    #params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
    response = requests.post(url, data=data, headers=headers)
    resp = response.json()
    return resp

for line in get_response():
    line["id"]
    line["type"]
    #line["phone"]
    #line["phone2"]
    line["coordenades"]["latitude"]
    line["coordenades"]["longitude"]
    line["address"]["street"]
    line["address"]["number"]
    line["address"]["city"]
    line["address"]["province"]
    print(line["closest"])
    



    



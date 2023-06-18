from bs4 import BeautifulSoup
import json


def load_data(conection):
    pass

def get_data(html):
    bs4 = BeautifulSoup(html, "html.parser")
    items = bs4.find_all("td", {"dir": "ltr"})
    is_track = False
    k = 0
    map_data = {}
    list_data = []
    modality = 'day'
    
    for item in (items):
        

        if 'diurno' in item.text.lower():
            modality = 'day'
        
        if 'nocturno' in item.text.lower():
            modality = 'nigth'

        
        if item.text.isnumeric() and len(item.text) == 6:
            is_track = True
            k = 0

        if is_track:
            map_data[k] = item.text.capitalize()
            map_data['modality'] = modality
            

        if len(item.text) == 1:
            if map_data:
                is_track = False
                list_data.append(map_data.copy())
                map_data.clear()

        k += 1
    
    open("file.json", "w").write(json.dumps(list_data, indent=2))

PATH = "/home/riuz/Imágenes/semester.html"
data = open(PATH, "r").read()
get_data(data)

import requests,json
from elasticsearch import Elasticsearch
from datetime import datetime

#Prueba conexion
#res = requests.get('http://94.130.73.248:9200')

es = Elasticsearch([{'host': '94.130.73.248', 'port': 9200}])

def creaindex():
    r = requests.get('http://94.130.73.248:9200') 
    i = 1
    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
        i=i+1
    
    print(i)

creaindex()
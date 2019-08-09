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

def createindex(es):
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['result'])

createindex(es)
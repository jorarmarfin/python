import requests
res = requests.get('http://94.130.73.248:9200')

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '94.130.73.248', 'port': 9200}])
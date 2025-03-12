import requests


endpoint = "http://localhost:8000/api/"
getR = requests.get(endpoint, params= {"abc": 123}, json={'query': 'Hello world'})
print(getR.json())
# Consumir uma API publica de dogs, que retorna um status HTTP:     
import requests 

url_base = 'https://http.dog/'
endpoint = f' {url_base}/500.json'
resposta = requests.get(endpoint)
dog_api = resposta.json()
print ('Olha que legal esse dog: ', dog_api)

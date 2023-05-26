# Consumir mais uma API publica:
        
import requests 

url_base = 'https://http.dog/'
endpoint = f' {url_base}/500.json'


resposta = requests.get(endpoint)

dog_api = resposta.json()

print ('Olha que loco esse dog ', dog_api)
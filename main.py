import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

# abrimos a url
resposta = urlopen(url)

# carrega o javascrip
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
pais = dados['country']
regiao = dados['region']

print("Detalhes do seu IP externo\n")
print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nOrg: {org}')
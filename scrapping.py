import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

link = "https://guildstats.eu/character?nick="
char = input(str("Nome do char: "))
caminho = link+char+"#tab2"
url = caminho

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

qtd_hrs_mensal = soup.find('div', id='tab2').get_text().strip()
print(qtd_hrs_mensal)


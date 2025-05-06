import sqlite3
import json
import requests
from bs4 import BeautifulSoup
import scraperwiki

# Esempio: scarica una pagina di test
url = "https://dofusdb.fr/en/tools/treasure-hunt"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Estrazione banale per test
title = soup.title.string.strip() if soup.title else "No title found"

# Salva un risultato di prova
scraperwiki.sqlite.save(["url"], {"url": url, "title": title})

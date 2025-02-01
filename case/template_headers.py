from Sincity.Agent.header import header
from bs4 import BeautifulSoup
import requests

def init_request():
    head = header()
    url = 'https://n5m.ru/usagent.html'
    response = requests.get(url, headers=head)

    if response.status_code == 200:
        bs = BeautifulSoup(response.content, 'lxml')
        print(bs.h1.get_text())

init_request()


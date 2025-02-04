import requests, json, os, time
from SinCity.Proxy.check_dir import check_work_dir
from SinCity.Proxy.read_list_proxy import read_json
from bs4 import BeautifulSoup

list_dict = []

def collectet_proxy(processing_proxy:dict):
    global list_dict

    ip = processing_proxy.split(':')[0]
    port = processing_proxy.split(':')[1]
    data = {ip:port}
    list_dict.append(data)

def parser_proxy(proxy_url:str):
    response = requests.get(proxy_url)
    if response.status_code == 200:
        for proxy in response.text.splitlines():
            proxy = proxy.strip()
            if proxy and ':' in proxy:collectet_proxy(proxy)


def get_proxy():
    #фунция проверки существования директории для списка прокси в json
    check_work_dir()
    
    #получаем списки прокси
    list_http, list_https = read_json()
    
    list_proxie = [list_http, list_https]

    for proxies in list_proxie:
        for proxy in proxies:
            print(proxy)
            parser_proxy(proxy_url=proxy)
            time.sleep(2)
        
    
    print(len(list_dict))

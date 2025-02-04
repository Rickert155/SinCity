import requests, json, os
from SinCity.Proxy.check_dir import check_work_dir
from SinCity.Proxy.read_list_proxy import read_json


def get_proxy():
    #фунция проверки существования директории для списка прокси в json
    check_work_dir()
    
    #получаем списки прокси
    list_http, list_https = read_json()

    print(f'{list_http}\n{list_https}')

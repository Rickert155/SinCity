import json
from manifest import proxy_json_path

def add_proxy_to_list(proxy:str, list_proxy:str):
    list_proxy.append(proxy)

    return list_proxy

def read_json():
    list_http, list_https = [], []
    with open(proxy_json_path, 'r') as file:
        result = json.load(file)
        for proxy_http in result['http']:
            get_list_http = add_proxy_to_list(proxy=proxy_http, list_proxy=list_http)
        for proxy_https in result['https']:
            get_list_https = add_proxy_to_list(proxy=proxy_https, list_proxy=list_https)
    
    return list_http, list_https

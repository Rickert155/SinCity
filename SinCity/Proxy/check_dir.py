import os, json
from manifest import proxy_json_path, case_proxy_path

def check_work_dir():
    if not os.path.exists(case_proxy_path):
        os.makedirs(case_proxy_path)
    if not os.path.exists(proxy_json_path):
        with open(proxy_json_path, 'w') as file:
            data = {"http":[], "https":[]}
            json.dump(data, file, sort_keys=True, indent=4)

        print(f'Добавьте списки прокси: {proxy_json_path}')
    else:print(f'JSON для хранения прокси существует')

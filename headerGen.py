import requests
from proxyListGen import proxyListCheck
def buscarEn(url):
    try:
        triesList = []
        prox = proxyListCheck()
        proxy = f"{prox[0]}:{prox[1]}"
        session = requests.Session()
        while True:
            try:
                r = session.get(url, proxies={'http':proxy, 'https':proxy}, timeout=7)
                break 
            except requests.exceptions.RequestException as err:
                triesList.append(proxy)
                prox = proxyListCheck()
                proxy = f"{prox[0]}:{prox[1]}"
                if proxy in triesList:
                    while proxy not in triesList:
                        prox = proxyListCheck() 
                        proxy = f"{prox[0]}:{prox[1]}"
                session = requests.Session()
        if r.status_code == 200:
            return proxy
        else:
            while True:
                try:
                    r = session.get(url, proxies={'http':proxy, 'https':proxy}, timeout=3)
                    break
                except requests.exceptions.RequestException as err:
                    triesList.append(proxy)
                    prox = proxyListCheck()  
                    proxy = f"{prox[0]}:{prox[1]}"
                    if proxy in triesList:
                        while proxy not in triesList:
                            prox = proxyListCheck()
                            proxy = f"{prox[0]}:{prox[1]}"
                    session = requests.Session()     
            return proxy        
    except requests.exceptions.RequestException as err:
        print(err, 'HeaderGen')

 
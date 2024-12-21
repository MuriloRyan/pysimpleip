# pysimpleip

a simple python website that uses https://ipquery.io/ api to create IP address queries on the web

it runs using **python** and **flask**

due some issues trying to use ipquery python lib

I created an simple python class for the queries

take a look:

```Python3
import requests

class IpQueryClient:
    def __init__(self) -> None:
        self.url = 'https://api.ipquery.io/'

    def own_ip(self) -> requests.Response:
        req = requests.get(self.url)
        return req
    
    def get_ip(self, ip: str) -> requests.Response:
        req = requests.get(self.url + ip)
        return req
    
    def get_more(self, ips: list) -> requests.Response:
        req = requests.get(self.url + ','.join(ips))
        return req
```
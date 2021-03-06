#!/bin/python3

import requests 
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    auth=('devnetuser', 'Cisco123!'))
    
response.raise_for_status()
payload=response.json()
pprint(payload)

token=response.json()['Token']
response = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
    headers={'X-Auth-Token':token}
)
payload=response.json()
pprint(payload)

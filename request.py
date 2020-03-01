#!/bin/python3

import requests 
from pprint import pprint

response = requests.post(
    'https://sandboxnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXN1cjpDaXNjbzEyMyE='})
    
payload=response.json()
pprint(payload)
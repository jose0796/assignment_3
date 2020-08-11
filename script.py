import requests
import json
import sys

URL = 'https://sandboxsdwan.cisco.com:8443/dataservice/device'
res = requests.get(URL, verify=False, auth=('devnetuser', 'Cisco123!'))

gson = res.json()

for item in gson['data']:
    print('--------------------')
    print("host_name: ", item['host-name'])
    print("device_type: ", item['device-type'])
    print('status: ', item['status'])

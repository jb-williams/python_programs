#!/usr/bin/env python3

import requests

response = requests.get('https://httpbin.org/ip')
print('IP: {0}'.format(response.json()['origin']))

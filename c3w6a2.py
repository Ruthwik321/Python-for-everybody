import json
from urllib.request import urlopen
import urllib.parse
import re

param=dict()
param['key']=42
param['address']=input('Enter address')
url='http://py4e-data.dr-chuck.net/json?'+urllib.parse.urlencode(param)
data=urlopen(url).read().decode()
js=json.loads(data)
#print(json.dumps(js,indent=4))

print(js['results'][0]['place_id'])

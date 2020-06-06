from urllib.request import urlopen
import json

data=urlopen('http://py4e-data.dr-chuck.net/comments_558548.json').read().decode()
js=json.loads(data)
#print(json.dumps(js,indent=4))
sum=0
for i in js['comments']:
    sum+=i['count']
print(sum)

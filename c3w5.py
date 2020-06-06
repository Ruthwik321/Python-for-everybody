from urllib.request import urlopen
import xml.etree.ElementTree as ET

xs=urlopen('http://py4e-data.dr-chuck.net/comments_558547.xml').read()
tree=ET.fromstring(xs)
l=tree.findall('comments/comment')
sum=0
for i in l:
    #print(i.find('count').text)
    sum+=int(i.find('count').text)

print(sum)

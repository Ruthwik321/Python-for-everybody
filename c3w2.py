import re

handle=open('regex_sum_42.txt')
l=[]
for i in handle:
    x=re.findall("[0-9]+",i)
    l.extend(x)
l=list(map(int,l))
print(l)
print()
print(sum(l))

#name=input('Enter file name')
h=open("mbox-short.txt")
d={}
for i in h:
    if i.startswith('From '):
        x=i.split()
        t=x[-2][:2]
        d[t]=d.get(t,0)+1
l=list(d.items())
l.sort()
for i,j in l:
    print(i,j)

n=input()
a=n.replace(" ","")
b=a.lower()
d={}
for i in b:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
count=0
c=list(d.values())
for i in c:
    if i==1:
        count=count+1
print(count)
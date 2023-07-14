n=input()
a=n.replace(" ","")
b=a.lower()
c=set(b)
d=""
for i in c:
    d=d+i
e=sorted(d)
print("".join(e))
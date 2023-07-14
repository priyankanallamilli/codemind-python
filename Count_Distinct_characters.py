n=input()
b=n.replace(" ", "")
c=b.lower()
a=set(c)
c=0
for i in a:
    c+=1
print(c)
a=input()
b="0123456789"
c=0
for i in a:
    if i in b:
        c+=1
if c>0:
    print("Contains "+str(c)+" digit")
else:
    print("Doesn't contain digit")
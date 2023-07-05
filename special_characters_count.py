n=input()
a="abcdefghijklmnopqrstuvwxyz0123456789 "
b=n.lower()
c=0
for i in b:
    if i not in a:
        c=c+1
print(c)
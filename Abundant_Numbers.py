n=int(input())
c=[]
for i in range(1,n):
    if n%i==0:
        c.append(i)
d=sum(c)
if d>n:
    print("True")
else:
    print("False")
    
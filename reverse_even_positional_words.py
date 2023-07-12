n=input()
a=n.split()
for i in range(len(a)):
    if i%2==0:
        b=str(a[i])
        c=b[::-1]
        print(c,end=" ")
    else:
        print(a[i],end=" ")
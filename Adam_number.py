def rev(n):
    d=0
    while n!=0:
        r=n%10
        d=d*10+r
        n=n//10
    return d
n=int(input())
e=n*n
f=rev(n)
g=f*f
h=rev(g)
if h==e:
    print("True")
else:
    print("False")

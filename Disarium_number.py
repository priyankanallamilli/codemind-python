n=int(input())
temp=n
a=len(str(temp))
d=0
while n:
    r=n%10
    d=d+r**a
    a=a-1
    n=n//10
if d==temp:
    print("True")
else:
    print("False")
n=int(input())
temp=n
b=len(str(n))
d=0
while n:
    r=n%10
    d=d+r**b
    b=b-1
    n=n//10
if d==temp:
    print("True")
else:
    print("False")
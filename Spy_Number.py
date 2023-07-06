n=int(input())
a=0
p=1
while n>0:
    d=n%10
    a=a+d
    p=p*d
    n=n//10
if a==p:
    print("Spy Number")
else:
    print("Not Spy Number")
    
    
n=int(input())
a=0
b=1
c=0
count=0
for i in range(n):
    a=b
    b=c
    c=a+b
    if c==n:
        count=1
if count==1:
    print("True")
else:
    print("False")
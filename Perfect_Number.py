n=int(input())
count=0
for i in range(1,n):
    a=n%i
    if a==0:
        count=count+i
if(count==n):
    print("True")
else:
    print("False")
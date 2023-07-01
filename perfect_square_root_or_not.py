n=int(input())
c=0
for i in range(n):
    if n==i*i:
        c=1
if c==1:
    print("True")
else:
    print("False")
n=int(input())
c=0
k="1234567890"
for i in range(n):
    a=input()
    c=0
    for i in a:
        if i not in k:
            c+=1
    if c==0:
        print("True")
    else:
        print("False")
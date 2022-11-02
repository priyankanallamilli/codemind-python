x=int(input())
for i in range (1,x+1):
    c=0
    a=int(input())
    for h in range(1,a+1):
        if h*h==a:
            c=1
    if c==0:
        print("False")
    else:
        print("True")
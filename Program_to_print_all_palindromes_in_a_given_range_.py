x=int(input())
y=int(input())
for i in range(x,y+1):
    temp=i
    c=0
    while(temp>0):
        r=temp%10
        c=(c*10)+r
        temp=temp//10
        if(i==c):
            print(i,end=' ')
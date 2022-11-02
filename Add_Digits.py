def add(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    if sum<=9:
        return sum
    else:
        return add(sum)
n=int(input())
print(add(n))
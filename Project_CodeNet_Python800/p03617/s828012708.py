import decimal
a,b,c,d=map(int,input().split())
n=int(input())
l=[a*4,b*2,c,d/2]
p=min(l)
q=min(l[:3])
print(int(decimal.Decimal(n)*decimal.Decimal(min(l))) if n%2==0 or p==q else int(decimal.Decimal(n-1)*decimal.Decimal(d/2)+q))
N = int(input())

ans = N
digit = 0
while ans>0:
    tmp = ans%10
    digit += tmp
    ans = ans//10

if N%digit==0:
    print('Yes')
else:
    print('No')
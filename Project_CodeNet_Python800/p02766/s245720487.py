n,k = map(int,input().split())
count = 1
while k<=n:
    n //= k
    count += 1
print(count)
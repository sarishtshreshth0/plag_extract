N,K = map(int, input().split())
tmp=N
count=0
while tmp!=0:
    tmp = tmp//K
    count += 1

print(count)
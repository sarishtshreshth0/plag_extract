n,k= map(int,input().split())
temp = 1 
cnt = 0

while n >= temp:
    temp *= k
    cnt += 1
print(max(1,cnt))
n = int(input())
lis = list(map(int, input().split()))

lis = sorted(lis)

count = [0]*100001

for i in range(n):
    count[lis[i]] += 1

ans = 0

for j in range(1,100000):
    t = count[j-1]+ count[j]+ count[j+1]
    ans = max(ans, t)
    
print(ans)
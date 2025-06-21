n,d = map(int, input().split())
a = []
ans = 0

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1,n):
        sum = 0
        for v1, v2 in zip(a[i], a[j]):
            sum += (v1-v2)**2
        sum**=0.5
        #print(sum)
        if sum == int(sum):
            ans += 1

print(ans)
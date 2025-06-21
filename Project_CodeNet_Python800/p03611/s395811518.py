n = int(input())
a = list(map(int, input().split()))

num = [0]*(10**5 + 1)

for x in a:
    num[x] += 1

ans = num[0] + num[1] + num[2]

for i in range(1, 10**5):
    tmp = num[i-1] + num[i] + num[i+1]
    if tmp > ans:
        ans = tmp

print(ans)

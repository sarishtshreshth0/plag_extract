N = int(input())
a = list(map(int,input().split()))
table = [0 for _ in range(100001)]
for i in a:
    table[i] += 1
ans = [0 for _ in range(100001)]
for j in range(1,100000):
    ans[j] = table[j-1]+table[j] + table[j+1]
print(max(ans))
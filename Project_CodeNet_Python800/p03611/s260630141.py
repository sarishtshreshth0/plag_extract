n = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(10 ** 5 + 3)]
for num in a:
    ans[num] += 1
    ans[num + 1] += 1
    ans[num + 2] += 1
print(max(ans))
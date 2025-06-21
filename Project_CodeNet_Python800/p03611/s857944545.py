n = int(input())

a = list(map(int, input().split()))
ans = [0] * (max(a) + 2)

for i in a:
  ans[i] += 1
  ans[i + 1] += 1
  if i - 1 >= 0:
    ans[i - 1] += 1
print(max(ans))
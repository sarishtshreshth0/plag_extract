n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
if n >= m:
  print(0)
  exit()
diff = sorted([lst[i + 1] - lst[i] for i in range(m - 1)], reverse=True)
print(sum(diff[n - 1:]))
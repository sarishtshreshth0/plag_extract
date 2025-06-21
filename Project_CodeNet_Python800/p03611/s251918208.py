n = int(input())
lst = list(map(int, input().split()))
dic = {}
for i in range(n):
  a = lst[i]
  dic.setdefault(a - 1, 0)
  dic[a - 1] += 1
  dic.setdefault(a, 0)
  dic[a] += 1
  dic.setdefault(a + 1, 0)
  dic[a + 1] += 1
print(max(list(dic.values())))
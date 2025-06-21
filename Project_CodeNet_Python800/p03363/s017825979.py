n = int(input())
a = list(map(int, input().split()))

count_list = {}
s = 0
for i in range(n):
  s += a[i]
  count_list[s] = count_list.get(s, 0) + 1

count = 0
count += count_list.get(0, 0) * (count_list.get(0, 0)+1)
for i in count_list.keys():
  if i!=0:
    #count+= count_list[i] * count_list.get(-i, 0)
    count += count_list[i] * (count_list[i]-1)
print(count//2)
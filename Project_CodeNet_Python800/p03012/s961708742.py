count = int(input())
arr = input().split()
s1 = 0
s2 = 0
for i in arr:
  s2 += int(i)
minimum_diff = s2
for i in range(0, count):
  s1 += int(arr[i])
  s2 -= int(arr[i])
  minimum_diff = min(minimum_diff, abs(s1-s2))
  
print(minimum_diff)

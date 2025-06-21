n = int(input())
list1 = list(map(int, input().split()))
great = 9999999
for i in range(n - 1):
  temp = int(abs(sum(list1[:i + 1]) - sum(list1[i + 1:])))
  if temp < great:
    great = temp
print(great)

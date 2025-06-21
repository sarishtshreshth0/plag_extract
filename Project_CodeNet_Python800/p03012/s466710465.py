a = input()
b = list(map(int, input().split()))
min = 100000
 
for i in range(len(b)):
  left = 0
  right = 0
  for j in range(i+1):
    left += b[j]
  for j in range(i+1, len(b)):
    right += b[j]
  if min > abs(left - right):
    min = abs(left - right)
    
print(min)
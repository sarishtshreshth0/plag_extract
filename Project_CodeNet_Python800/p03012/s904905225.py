n =int(input())
min_value =1000000000000000000000000000
w = list(map(int,input().split()))
for i in range(n):
  a = sum(w[0:i])
  b = sum(w[i:n])
  if abs(a - b) < min_value:
    min_value = abs(a-b)
print(min_value)
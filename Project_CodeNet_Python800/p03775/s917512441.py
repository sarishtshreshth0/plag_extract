n = int(input())

m = int(n**0.5)+1
while m:
  if n%m == 0:
    a = len(str(m))
    b = len(str(n//m))
    break
  else: m -= 1
print(max(a,b))
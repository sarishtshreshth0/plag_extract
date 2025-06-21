n = int(input())
s = input()
memo = ""
for i in s:
  if memo == i:
    n-=1
  else:
    memo=i
print(n)
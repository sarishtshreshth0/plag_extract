n = int(input())
s = input()
count = 1
for i in range(n-1):
  if s[i+1]  != s[i]:
    count = count + 1
print(count)
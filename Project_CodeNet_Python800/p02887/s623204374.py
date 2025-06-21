n = int(input())
s = input()

i = 0
count = 0
while i < n:
  c = s[i]
  while i < n and s[i] == c:
    i += 1
  count += 1
print(count)
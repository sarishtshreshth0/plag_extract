n = int(input())
s = input()
temp = ''
cnt = 0
for i in s:
  if i != temp:
    cnt += 1
    temp = i
print(cnt)
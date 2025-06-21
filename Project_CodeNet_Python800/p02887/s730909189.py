n = int(input())
s = input()
prev_char = ""
result = 0

for i in s:
  if (prev_char != i):
    result += 1
  prev_char = i

print(result)
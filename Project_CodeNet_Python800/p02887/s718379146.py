a = int(input())
b = input()
c = 1
for i in range(a-1):
  if b[i] != b[i+1]:
    c += 1
print(c)

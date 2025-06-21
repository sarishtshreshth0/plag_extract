A, B = map(int, input().split())
for C in range(1, 3+1):
  if A * B * C % 2 == 1:
    print("Yes")
    exit()
print("No")
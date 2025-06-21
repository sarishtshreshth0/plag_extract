n = int(input())
used = []
bef = input()
used.append(bef)
for _ in range(n - 1):
  now = input()
  if now in used:
    print("No")
    exit()
  elif bef[-1] != now[0]:
    print("No")
    exit()
  else:
    used.append(now)
    bef = now
print("Yes")
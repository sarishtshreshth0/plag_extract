N = int(input())
l = []
for a in range(1, 10**5+1):
  if N % a == 0:
    b = N // a
    s = max(len(str(a)), len(str(b)))
    l.append(int(s))
print(min(l))
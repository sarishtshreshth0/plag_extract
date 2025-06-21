n = int(input())
a = 10**10
for i in range(1, int(n**.5) + 1):
  if n % i == 0:
    a = min(a, max(len(str(i)), len(str(int(n/i)))))
print(a)
N = int(input())
I = int(N**(0.5)//1)
a = []
for i in range(1, I+1):
  if N%i==0:
    j=N//i
    i = len(list(str(i)))
    j = len(list(str(j)))
    k = max(i, j)
    a.append(k)
print(min(a))
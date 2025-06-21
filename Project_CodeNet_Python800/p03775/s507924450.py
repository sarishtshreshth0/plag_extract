N = int(input())
r_N = int(N ** (1 / 2))
 
li = []
for n in range(1,r_N + 1):
  if N % n == 0:
    a = N // n
    l = max(len(str(a)),len(str(n)))
    li.append(l)
    
print(min(li))
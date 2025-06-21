N = int(input())
a = 100

for n in range(1,1+10**5):
  if N%n==0:
    a = min(a,max(len(str(n)),len(str(N//n))))

print(a)
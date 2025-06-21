M = int(input())
N=str(M)
fx=0
for a in N:
  fx+=int(a)
print('Yes' if M%fx==0 else 'No')
n = int(input())
f = 0
n_ = n
for i in range(len(str(n))-1,-1, -1):
    f += n_//(10**i) 
    n_ %= (10**i)

if n%f == 0:
    print("Yes") 
else:
    print("No")
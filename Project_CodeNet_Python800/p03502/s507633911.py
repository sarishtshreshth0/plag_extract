N = input()
Nls = list(map(int,N))
f = 0
N = int(N)
for i in Nls :
    f += i
if N%f==0 :
    print("Yes")
else :
    print("No")
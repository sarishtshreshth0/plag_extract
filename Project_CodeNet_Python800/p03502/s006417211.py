N = int(input())
Temp = str(N)
L = len(Temp)
Sl = list(Temp)
S = 0
for i in range(L):
    S += int(Sl[i])
if (N%S == 0):
    print("Yes")
else:
    print("No")
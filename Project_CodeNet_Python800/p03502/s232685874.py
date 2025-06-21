n = list(input())
N = ""
M = 0

for i in range(len(n)):
    N += n[i]
    M += int(n[i])

N = int(N)

if N % M == 0:
    print("Yes")
else:
    print("No")

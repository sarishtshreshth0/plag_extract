N = list(input())
s = 0
for i in range(len(N)):
    s += int(N[i])
if int("".join(N)) % s == 0:
    print("Yes")
else:
    print("No")

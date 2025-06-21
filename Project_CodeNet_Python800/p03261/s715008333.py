N = int(input())
W = [input() for _ in range(N)]
if len(W) != len(set(W)):
    print("No")
    exit()

f = True
for i in range(len(W)-1):
    if W[i][-1] != W[i+1][0]:
        f = False

if not f:
    print("No")
else:
    print("Yes")
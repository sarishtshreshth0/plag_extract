import sys
input = lambda : sys.stdin.readline().rstrip()

m, d = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(1, d + 1):
        if len(str(j)) >= 2 and int(str(j)[0]) >= 2 and int(str(j)[1]) >= 2 and int(str(j)[0])*int(str(j)[1]) == i:
            #print(i, j)
            ans += 1
print(ans)
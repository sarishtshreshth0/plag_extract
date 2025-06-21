n = int(input())
w = [input() for _ in range(n)]
import sys
li = [w[0]]
for i in range(n-1):
    if w[i+1][0]!=w[i][-1]:
        break
    if w[i+1] in li:
        break
    else:
        li.append(w[i+1])
else:
    print("Yes")
    sys.exit()
print("No")
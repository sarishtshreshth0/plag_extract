n = int(input())
w = [input() for i in range(n)]
f = 0
for i in range(n-1):
    if w[i][len(w[i])-1] != w[i+1][0]:
        f = 1
    for j in range(n):
       if j != i:
            if w[i] == w[j]:
                f = 1
if f==1:
    print('No')
else:
    print('Yes')
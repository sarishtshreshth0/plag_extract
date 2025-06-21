n = int(input())
w = []
flag = 0
tmp = ''

for i in range(n):
    w.append(input())
    if i == 0:
        continue
    elif w[i][0] != w[i-1][len(w[i-1])-1]:
        flag = 1

w = sorted(w)

for i in range(1,n):
    if w[i-1] == w[i]:
        flag = 1
        break

if flag == 0:
    print('Yes')
else:
    print('No')

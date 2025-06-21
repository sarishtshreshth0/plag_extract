n = int(input())
w = [str(input()) for i in range(n)]
z = 'Yes'
l = [w[0]]
for h in range(n-1):
    if w[h][-1] == w[h+1][0] and w[h+1] not in l:
        l.append(w[h+1])
    else:
        z = 'No'
        break
print(z)
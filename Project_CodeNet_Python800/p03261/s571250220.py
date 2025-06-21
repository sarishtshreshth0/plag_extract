n = int(input())
wl = []
for _ in range(n):
    wl.append(input())



word0 = wl[0][-1]

for i in range(1,n):
    if wl[i][0] == word0 and wl[i] not in wl[:i]:
        word0 = wl[i][-1]
    else:
        print('No')
        exit()
print('Yes')
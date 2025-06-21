
n = int(input())
v = []
for i in range(n+1):
    v.append([])

colorv = [None] * (n+1)

for i in range(n-1):
    a,b = map(int, input().split())
    v[a].append([b,i])
    v[b].append([a,i])

for cur in range(1, n+1):

    #print("cur", cur)

    used = dict()

    for i in range(len(v[cur])):
        next, linenum = v[cur][i]
        if colorv[linenum] is None:
            continue
        #print(" line", linenum, "is", colorv[linenum])
        used[colorv[linenum]] = True

    ncolor = 1

    for i in range(len(v[cur])):
        next, linenum = v[cur][i]
        if colorv[linenum] is not None:
            continue
        while ncolor in used:
            ncolor += 1
        colorv[linenum] = ncolor
        #print(" set line", linenum, "is", ncolor)
        used[ncolor] = True

print(max(colorv[:-2]))
for i in range(n-1):
    print(colorv[i])
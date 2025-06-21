def is_753(n):
    n = str(n)
    return(n.count("7") >= 1 and n.count("3") >= 1 and n.count("5") >= 1)


n = int(input())


v = [7, 5, 3]
li = []
prev = [7, 5, 3]

for i in range(9):
    tmp = []
    for j in v:
        for k in prev:
            tmp.append(k * 10 + j)
    prev = tmp
    li = li + prev

li = [x for x in li if is_753(x) and x <= n]

print(len(li))
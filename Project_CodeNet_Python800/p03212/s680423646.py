def make753(n):
    ns = str(n)
    l = len(ns)* -1
    flg = True
    while flg:
        for i in range(-1, l-1, -1):
            if ns[i] == '3' or ns[i] == '5':
                ii = (i+1)*-1
                n += 10**ii*2
                flg = False
                break
            if ns[i] == '7':
                ii = (i+1)*-1
                n -= 10**ii*4
                flg = False
                continue
    ns = str(n)
    for j in range(len(ns)):
        if not ns[j] == '3':
            break
        if j == len(ns) - 1:
            n = 10*n+3
    return n


def check753(n):
    ns = str(n)
    l = len(ns)
    a = []
    for i in range(l):
        a.append(int(ns[i]))
    a = list(set(a))
    if len(a) == 3:
        return True
    else:
        return False

n = int(input())
a = 333
cnt = 0

while a <= n:
    if check753(a):
        cnt += 1
    a = make753(a)
print(cnt)
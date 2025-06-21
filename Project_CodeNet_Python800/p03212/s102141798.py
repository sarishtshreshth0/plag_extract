A = []
str = "357"
lim = 11

def dfs(bef, sz):
    if sz + 1 == lim:
        return
    for i in str:
        t = bef + i
        A.append(t)
        dfs(t, sz + 1)

def main():
    n = int(input())

    dfs("", 0)

    ans = 0

    for a in A:
        q = False
        w = False
        e = False
        for i in a:
            if i == '3':
                q = True
            elif i == '5':
                w = True
            elif i == '7':
                e = True
        if q and w and e:      
            ai = int(a)
            if ai <= n:
                ans += 1

    print(ans)

main()
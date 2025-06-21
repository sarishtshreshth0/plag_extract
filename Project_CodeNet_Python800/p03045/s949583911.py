def main():
    n,m = map(int,input().split())
    g = {}
    for i in range(m):
        x,y,z = map(int,input().split())
        if x-1 not in g.keys():
            g[x-1] = [y-1]
        else:
            g[x-1] += [y-1]
        if y-1 not in g.keys():
            g[y-1] = [x-1]
        else:
            g[y-1] += [x-1]
    t = [-1 for i in range(n)]
    def bfs(s,t):
        t[s] = 0
        que = [s]
        while len(que)>0:
            v = que.pop(0)
            for nv in g[v]:
                if t[nv]!=-1:
                    continue
                t[nv]=0
                que.append(nv)
        return t

    ans = 0
    for i in range(n):
        s = i
        if t[s]!=-1:
            continue
        if s not in g.keys():
            ans += 1
            continue
        t[s]=0
        ans += 1
        t = bfs(s,t)
    print(ans)

if __name__ == "__main__":
    main()

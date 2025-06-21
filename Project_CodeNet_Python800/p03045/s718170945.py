def main():
    n,m = map(int,input().split())
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for i in range(m):
        x,y,z = map(int,input().split())
        graph[x] += [y]
        graph[y] += [x]
    dis = [-1 for i in range (n)]
    ans = 0
    for i in range(n):
        if dis[i]==-1:
            ans += 1
            que = [i]
            dis[i] = 0
            while len(que)>0:
                s = que.pop(0)
                for nv in graph[s+1]:
                    if dis[nv-1]!=-1:
                        continue
                    dis[nv-1] = 0
                    que.append(nv-1)
    print(ans)
    
if __name__ == "__main__":
    main()

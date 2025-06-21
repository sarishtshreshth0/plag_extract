from collections import deque

N = int(input())

def bfs(s):
    que = deque()
    que.append(s)
    cnt = 0
    while que.__len__() != 0:
        s = que.popleft()
        for ds in '753':
            ss = s + ds
            if int(ss) > N:
                continue
            if all(ss.count(i) > 0 for i in '753'):
                cnt += 1
            que.append(ss)
    return cnt

ans = 0
ans += bfs('3')
ans += bfs('5')
ans += bfs('7')

print(ans)

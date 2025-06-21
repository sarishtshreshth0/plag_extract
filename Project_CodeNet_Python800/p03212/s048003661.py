from collections import deque

def check753(num):
    three = False
    five = False
    seven = False
    for s in num:
        if s == "3":
            three = True
        elif s == "5":
            five = True
        elif s == "7":
            seven = True
        if three and five and seven:
            return True
    return False

n = int(input())

q = deque([3,5,7])

ans = 0
while q:
    now = q.popleft()
    
    t = "".join([str(now), "3"])
    if int(t) <= n:
        q.append(int(t))
        if check753(t):
            ans += 1
    f = "".join([str(now), "5"])
    if int(f) <= n:
        q.append(int(f))
        if check753(f):
            ans += 1
    s = "".join([str(now), "7"])
    if int(s) <= n:
        q.append(s)
        if check753(s):
            ans += 1
print(ans)
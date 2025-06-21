import sys,collections
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
ac = collections.Counter(a)
dc = sorted(ac.items(),key = lambda x:(-x[1],x[0]))

ans = 0
for i in range(len(dc)):
    key = dc[i][0]
    val = dc[i][1]
    if ans > 3*val:
        print(ans)
        exit()
    ans = max(ans,ac[key-1]+ac[key]+ac[key+1])
print(ans)

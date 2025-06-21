n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

dic = {}
for a in al:
    dic[a] = dic.get(a, 0)+1

mx = max(al)
mn = min(al)
ans = 0
for x in range(mn, mx+1):
    ans = max(ans, dic.get(x+1, 0)+dic.get(x, 0)+dic.get(x-1, 0))
print(ans)

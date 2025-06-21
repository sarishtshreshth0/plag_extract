from operator import itemgetter
Q, H, S, D = map(int, input().split())
p = sorted([(1,Q,Q*8),(2,H,H*4),(4,S,S*2),(8,D,D)], key=itemgetter(2))
N = int(input()) * 4
ans = 0
for i in range(4):
    ans += N // p[i][0] * p[i][1]
    N -= N // p[i][0] * p[i][0]
print(ans)

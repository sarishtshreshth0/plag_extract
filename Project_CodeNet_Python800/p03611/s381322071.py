
N = int(input())
a = list(map(int,input().split()))
a = sorted(a)

cnt=[0]*(a[-1]+2)
for i in range(N):
    cnt[a[i]]+=1

out=0
dam = cnt[0] + cnt[1]
out=max(out,dam)
for i in range(1,a[-1]+1):
    dam = cnt[i-1] + cnt[i] + cnt[i+1]
    out=max(out,dam)
print(out)
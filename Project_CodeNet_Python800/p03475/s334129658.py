n = int(input())
pair = []
ns = []
for i in range(n-1):
    c,s,f = map(int, input().split())
    pair.append((c,s,f))

ans = []
for i in range(n-1):
    c,s,f = pair[i]
    cnt = s + c
    for j in range(i+1,n-1):
        c,s,f = pair[j]
        s_ = max(s,((cnt - 1)//f+1)*f)
        cnt = s_ + c
    print(cnt)
print(0)
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

if N >= M:
    print(0)
    exit()

org_kyori =[]
for i in range(len(arr)-1):
    org_kyori.append(arr[i+1]-arr[i])

kyori =sorted(org_kyori)

ans = sum(kyori)
for i in range(N-1):
    ans -= kyori[-1*(i+1)]

print(ans)


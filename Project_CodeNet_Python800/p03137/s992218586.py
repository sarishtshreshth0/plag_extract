N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

if N >= M :
    print(0)
    exit()

sub = []
for i in range(1,M):
    sub.append(X[i]-X[i-1])
sub = sorted(sub)

if N == 1:
    print(sum(sub))
else:
    ans = sum(sub[:-(N-1)])
    print(ans)




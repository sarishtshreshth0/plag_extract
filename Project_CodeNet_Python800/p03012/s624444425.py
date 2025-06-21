n = int(input())
w = tuple(map(int, input().split()))
av_min = 100000
for i in range(n-1):
    av = abs(sum(w[:i+1]) - sum(w[i+1:]))
    if av < av_min:
        av_min = av
    else:
        break
print(av_min)
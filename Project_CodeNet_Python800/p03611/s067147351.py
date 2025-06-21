N = int(input())
a_s = list(map(int,input().split()))
cnt = [0] * (max(a_s)+1)
for a in a_s:
    cnt[a] += 1
answer = 1
for i,c in enumerate(cnt):
    if i < 1:
        answer = max(answer, cnt[i])
        continue
    if i < 2:
        answer = max(answer, sum(cnt[i-1:i+1]))
        continue
    answer = max(answer, sum(cnt[i-2:i+1]))
print(answer)
from collections import Counter
N = int(input())
A_s = list(map(int,input().split()))
ruiseki = [0]
for i,a in enumerate(A_s):
    ruiseki.append(ruiseki[i]+a)
counter = Counter(ruiseki)


answer = 0
for k,v in counter.items():
    if v > 1:
        answer += v * (v-1)//2
print(answer)
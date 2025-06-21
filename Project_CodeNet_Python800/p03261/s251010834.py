N = int(input())
W = []
answer = 'Yes'
for i in range(N):
    W.append(input())

for i in range(N - 1):
    if W.count(W[i]) > 1:
        answer = 'No'
        break
    if W[i][-1] != W[i+1][0]:
        answer = 'No'
        break
print(answer)
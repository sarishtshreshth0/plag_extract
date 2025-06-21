N = int(input())
W = [input()]
ans = 1
for i in range(N-1):
    new_word = input()
    if new_word in W:
        ans = 0
        break
    W.append(new_word)
    if W[i][-1]!=W[i+1][0]:
        ans = 0
        break

for j in range(N-i-2):
    input()

if ans == 0:
    print('No')
else:
    print('Yes')

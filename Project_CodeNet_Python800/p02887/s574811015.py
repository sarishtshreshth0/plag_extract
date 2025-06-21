N = int(input())
S = list(input())

while(True):
    count = 0
    for i in range(len(S) - 1, 0, -1):
        if S[i] == S[i-1]:
            S.pop(i)
            count += 1
    if count == 0: break
print(len(S))
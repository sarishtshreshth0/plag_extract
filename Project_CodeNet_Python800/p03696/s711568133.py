N = int(input())
T = input()
S = list(T)
G = True
while G:
    G = False
    for i in range(1, len(S)):
        if S[i - 1] == '(' and S[i] == ')':
            S.pop(i)
            S.pop(i - 1)
            G = True
            break
for s in S:
    if s == '(':
        T = T + ')'
    else:
        T = '(' + T
print(T)
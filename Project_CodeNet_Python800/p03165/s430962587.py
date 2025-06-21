import sys
input = sys.stdin.readline

s = list(input())
t = list(input())
n = len(s)-1
m = len(t)-1
value = [[0]*(m+1) for i in range(n+1)]


for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            value[i + 1][j + 1] = value[i][j] + 1
        elif value[i][j + 1] > value[i + 1][j]: #UP
            value[i + 1][j + 1] = value[i][j + 1]
        else:  # LEFT
            value[i + 1][j + 1] = value[i + 1][j]
i = n-1
j = m-1
ans=""
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        ans = s[i] + ans
        i -= 1
        j -= 1
    elif value[i][j + 1] > value[i + 1][j]:
        i -= 1
    else:
        j -= 1
print(ans)

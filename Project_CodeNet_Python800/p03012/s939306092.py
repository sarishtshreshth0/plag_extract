n = int(input())
w = list(map(int,input().split()))


for i in range(n):
    a = sum(w[:i+1])
    b = sum(w[i+1:])
    if i == 0:
        s = abs(a-b)
    else:
        if abs(a-b) < s:
            s = abs(a-b)

print(s)
n = int(input())
a = list(map(int,input().split()))
s = [0]*(max(a)+4)
for i in a:
    s[i] += 1
    s[i+1] += 1
    s[i+2] += 1

print(max(s))
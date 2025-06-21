n = int(input())
a = list(map(int, input().split()))

l = [0] * 100002
for i in a:
    l[i+1] += 1
    l[i+2] += 1
    l[i] += 1
print(max(l))
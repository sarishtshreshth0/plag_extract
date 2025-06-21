N = int(input())
a = list(map(int,input().split()))

num = [0]*(10**5+1)
for i in a:
    if i-1 >= 0:
        num[i-1] += 1
    num[i] += 1
    if i+1 <= N:
        num[i+1] += 1

print(max(num))
N = str(input())
ans = 0
for n in list(N):
    ans += int(n)

if int(N)%ans==0:
    print('Yes')
else:
    print('No')
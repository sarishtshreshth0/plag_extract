n = int(input())
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
s = input()

ans = 1
last = s[0]
for i in range(1,n):
    if last != s[i]:
        last = s[i]
        ans = ans + 1

print(ans)



n = int(input())
s = input()
cur = s[0]
ans = 0
# if cur*n==s:
#     print(1)
# else:
for i in range(1,n):
    if s[i]==cur:
        pass
    else:
        cur = s[i]
        ans+=1
ans+=1
print(ans)
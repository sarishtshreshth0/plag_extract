n = int(input())

s = input()
ans = [s[0]]
for i in range(1,n):
    if ans[-1] != s[i] :
        ans.append(s[i])

print(len(ans))

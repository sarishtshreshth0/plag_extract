n=int(input())
s = input()
a = s[0]
cnt = 1
for i in range(n):
    if a == s[i]:
        continue
    else:
        a = s[i]
        cnt += 1
    
print(cnt)
n = int(input())
s = str(input())
w = s[0]
num = 0
for i in range(1,n):
    if w[0] == s[i]:
        w += s[i]
    else:
        num += 1
        w = s[i]
num += 1
print(num)
n = int(input())
s = input()

ans = ''
seek = 0

while seek < n:
    first = seek
    while seek < n and s[seek] == s[first]:
        seek += 1
    ans += s[first]

print(len(ans))

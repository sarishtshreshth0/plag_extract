s = input()
n = s[::2].count('0') + s[1::2].count('1')
ans = min(n, len(s) - n)
print(ans)
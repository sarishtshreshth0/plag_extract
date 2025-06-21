n = int(input())
s = input()
print(1 + sum(s[i] != s[i + 1] for i in range(n - 1)))
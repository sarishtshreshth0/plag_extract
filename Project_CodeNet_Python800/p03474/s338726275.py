a, b = map(int, input().split())
s = input()
t = s[:a] + s[-b:]
flg = s[a] == "-" and t.isdecimal()
print(["No", "Yes"][flg])
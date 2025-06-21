a, b = map(int, input().split())
s = input()
flg1 = s[:a].isdecimal()
flg2 = s[a] == "-"
flg3 = s[-b:].isdecimal()
flg = flg1 and flg2 and flg3
print(["No", "Yes"][flg])
a, b = map(int, input().split())
s = list(input())

if s[a] != "-":
    result = "No"
elif len([x for x in s if x in [str(x) for x in range(10)]]) + 1 == len(s):
    result = "Yes"
else:
    result = "No"
print(result)
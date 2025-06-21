a, b, c = input().strip().split(' ')
a, b, c = [int(a), int(b), int(c)]
if (a < c and b < c) or (a>c and b > c):
    ans = "No"
else:
    ans = "Yes"
print(ans)

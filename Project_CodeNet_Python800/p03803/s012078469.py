a, b = map(int, input().split())
ans = 'Draw'
if a == 1:
    if b != 1:
        ans = 'Alice'
elif b == 1:
    if a != 1:
        ans = 'Bob'
else:
    if a > b:
        ans = 'Alice'
    elif a < b:
        ans = 'Bob'
print(ans)

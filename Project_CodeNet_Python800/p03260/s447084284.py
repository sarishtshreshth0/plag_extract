a,b = map(int,input().split())
ans = 'No'

for i in range(1,3):
    if a * b * i % 2 != 0:
        ans = 'Yes'

print(ans)
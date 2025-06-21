A, B = list(map(int,input().split()))
ans = 'No'
for i in range(3):
    if A*B*(i+1)%2 == 1:
        ans = 'Yes'
        break
print(ans)
a,b = list(map(int, input().split()))
res = 'No' if (a%2==0) or (b%2==0) else 'Yes'
print(res)
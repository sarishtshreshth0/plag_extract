a, b = map(int,input().split())
print('Yes' if all(num%2==1 for num in [a,b]) else 'No')
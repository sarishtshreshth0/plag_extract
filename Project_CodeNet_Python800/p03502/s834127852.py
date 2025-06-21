n = int(input())

fx=sum(map(int, str(n)))
print('Yes' if n%fx==0 else 'No')
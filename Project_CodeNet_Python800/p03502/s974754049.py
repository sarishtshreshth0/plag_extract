n = input()
ns = sum(list(map(int, list(n))))
print('Yes' if int(n)%ns==0 else 'No')

N = int(input())
print('Yes' if N%sum(list(map(int, str(N)))) == 0 else 'No')
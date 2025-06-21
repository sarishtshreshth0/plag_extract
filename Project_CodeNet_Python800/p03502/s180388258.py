N = input()
print('Yes' if not int(N) % sum([int(x) for x in N]) else 'No')
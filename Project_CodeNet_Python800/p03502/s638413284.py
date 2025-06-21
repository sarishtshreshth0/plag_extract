N = input()
fN = sum([int(n) for n in N])
print('Yes' if int(N)%fN==0 else 'No')
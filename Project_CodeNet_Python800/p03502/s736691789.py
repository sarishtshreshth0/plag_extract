n = int(input())
ni = n
x = []
for i in range(10):
  x.append(ni // (10**(10 - i)))
  ni = n % (10 ** (10 - i))
x.append(ni % 10)
print('Yes' if n % sum(x) == 0 else 'No')
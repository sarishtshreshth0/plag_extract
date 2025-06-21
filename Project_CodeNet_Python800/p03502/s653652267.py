n = input()
print('Yes' if int(n) % sum([int(digit) for digit in n]) == 0 else 'No')
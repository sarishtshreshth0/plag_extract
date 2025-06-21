s = input()
n = int(s)
colsum = 0
for i in s:
    colsum += int(i)

print('Yes' if n%colsum == 0 else 'No')
n = input()
l = len(n)
counter = 0
for i in range(l):
    counter += int(n[i])
n = int(n)
if n % counter == 0: print('Yes')
else: print('No')
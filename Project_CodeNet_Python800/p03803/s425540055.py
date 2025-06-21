a = input().split(' ')
a[0] = int(a[0])
a[1] = int(a[1])

if (a[0] == 1): a[0] += 99
if (a[1] == 1): a[1] += 99

if (a[0] == a[1]): print("Draw")
elif (a[0]) > a[1]: print("Alice")
else: print("Bob")

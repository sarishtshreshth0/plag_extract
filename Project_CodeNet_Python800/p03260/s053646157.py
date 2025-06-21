line = input()
a, b = [int(n) for n in line.split()]
for n in range(1, 4):
    if (a*b*n)%2!=0:
        print("Yes")
        break
    if n==3:
        print("No")

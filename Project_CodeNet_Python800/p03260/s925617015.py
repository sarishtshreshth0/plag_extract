line = input()
a, b = [int(n) for n in line.split()]
ans = "No" if (a*b)%2 == 0 else "Yes"
print(ans)
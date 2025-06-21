n = int(input())

sol = n
for i in range(round(n**0.5), 1, -1):
    if n%i == 0:
        sol = n//i
        break

print(len(str(sol)))
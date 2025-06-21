n = int(input())
ln = list(str(n))
ln = [int(n) for n in ln]

total = sum(ln)
if n % total == 0:
    print("Yes")
else:
    print("No")
n = int(input())
total = sum(list(map(int, str(n))))
print ("Yes") if n%total == 0 else print ("No")

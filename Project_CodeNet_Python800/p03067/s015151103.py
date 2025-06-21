x = list(map(int,input().split()))
c = x[2]
print("Yes" if sorted(x)[1] == c else "No")
N = int(input())
sum_h = sum(int(x) for x in str(N))
print("Yes" if N % sum_h == 0 else "No")

A, B, C = map(int, input().split())
print("Yes" if (A-C)*(B-C)<=0 else "No")
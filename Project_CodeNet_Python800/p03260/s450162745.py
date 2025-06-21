A, B = map(int, input().split())
print("YNeos"[not (A * B) & 1::2])
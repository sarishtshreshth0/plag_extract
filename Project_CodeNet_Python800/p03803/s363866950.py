A, B = map(lambda x: (int(x)-2)%13, input().split())
print("Alice" if A > B else ("Draw" if A == B else "Bob"))
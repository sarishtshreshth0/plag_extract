a, b = map(lambda x: 14 if x == "1" else int(x), input().split())
print("Draw" if a == b else ("Alice" if a > b else "Bob"))
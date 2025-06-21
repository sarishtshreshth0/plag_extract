tmp = input().split(" ")
a = (int(tmp[0]) - 2) % 13
b = (int(tmp[1]) - 2) % 13
print("Alice") if a > b else print("Draw") if a == b else print("Bob")
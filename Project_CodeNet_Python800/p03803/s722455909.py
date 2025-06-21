a, b =map(int, input().split())
print("Alice" if a > b and b != 1 or a < b and a == 1
    else "Bob" if b > a and a != 1 or b < a and b == 1
    else "Draw")
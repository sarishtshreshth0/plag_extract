A,B = map(int, input().split())

A = (A + 11) % 13
B = (B + 11) % 13

print('Alice' if A > B else 'Draw' if A == B else 'Bob')
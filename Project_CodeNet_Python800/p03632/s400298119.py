A,B,C,D = map(int, input().split())

simultaneous_sec = 0
if A <= C:
    if B <= C:
        simultaneous_sec = 0
    else:
        simultaneous_sec = min(B, D) - C
else:
    if D <= A:
        simultaneous_sec = 0
    else:
        simultaneous_sec = min(B, D) - A
print(simultaneous_sec)
A,B,C,D = map(int, input().split())

Time = min(B,D) - max(A,C)

print(max(0, Time))
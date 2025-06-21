A, B, C, D = map(int, input().split())
dis = 0

if B <= C or D <= A:
  print(dis)
elif A <= C < B <= D:
  print(B-C)
elif C <= A < D <= B:
  print(D-A)
elif A <= C < D <= B:
  print(D-C)
elif C <= A < B <= D:
  print(B-A)
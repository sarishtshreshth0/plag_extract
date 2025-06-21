N, A, B = map(int, input().split())
S = input()

num_win = 0
num_win_f = 0
num_next = A + B
for s in S:
  if s == "a" and num_win < num_next:
    print("Yes")
    num_win += 1
  elif s == "b" and num_win < num_next and num_win_f < B:
    print("Yes")
    num_win += 1
    num_win_f += 1
  else:
    print("No")
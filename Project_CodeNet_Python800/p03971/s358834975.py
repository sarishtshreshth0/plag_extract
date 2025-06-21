N, A, B = map(int, input().split())
S = input()

count_all = 0
rank_b = 1
for c in S:
  if c == "a":
    if count_all < (A + B):
      print("Yes")
      count_all += 1
    else:
      print("No")
  elif c == "b":
    if count_all < (A + B) and (rank_b <= B):
      print("Yes")
      count_all += 1
      rank_b += 1
    else:
      print("No")
  elif c == "c":
    print("No")

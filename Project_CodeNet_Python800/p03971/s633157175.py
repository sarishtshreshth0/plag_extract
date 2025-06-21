N, A, B = [int(i) for i in input().split(" ")]
S = input()

cnt = 0
cnt_abroad = 0

for s in S:
  if A + B <= cnt:
    print("No")
    continue
  if s == "c":
    print("No")
    continue
  if s == "a":
    cnt += 1
    print("Yes")
    continue
  if s == "b":
    if B <= cnt_abroad:
      print("No")
      continue
    cnt += 1
    cnt_abroad += 1
    print("Yes")
    continue

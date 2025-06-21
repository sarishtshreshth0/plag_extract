N, A, B = map(int, input().split())
S = input()
n_passed = 0
n_passed_abroad = 1
for i, s in enumerate(S):
  res = "No"
  if s == 'a':
    if n_passed < A+B:
      res = "Yes"
      n_passed += 1
  elif s == 'b':
    if (n_passed < A+B) and (n_passed_abroad <= B):
      res = "Yes"
      n_passed += 1
      n_passed_abroad += 1

  print(res)
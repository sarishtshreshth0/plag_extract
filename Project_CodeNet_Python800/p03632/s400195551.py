A, B, C, D = map(int, input().split(' '))
answer = 0
if A <= C and B <= D:
  answer = B-C
if A <= C and B >D:
  answer = D-C
if A > C and B <= D:
  answer = B-A
if A > C and B > D:
  answer = D-A
if answer < 0:
  answer = 0
print(answer)
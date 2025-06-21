A, B, C, D = map(int, input().split(' '))
answer = min(B,D)-max(A,C) 
if answer < 0:
  answer = 0
print(answer)
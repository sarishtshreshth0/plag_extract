N, A, B = map(int, input().split())
S = str(input())

count = 0
count_B = 0

for n in range(N):
  if S[n] == "c":
    print("No")
    
  elif S[n] == "a":
    if count < A+B:
      print('Yes')
      count += 1
    else:
      print('No')
      
  elif S[n] == "b":
    if count < A+B and count_B < B:
      print('Yes')
      count += 1
      count_B += 1
    else:
      print('No')
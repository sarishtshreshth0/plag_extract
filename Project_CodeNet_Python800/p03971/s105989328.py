
N, A, B = list(map(int,input().split()))
S = input()
AB = A+B

pass_student = 0
B_pass_student = 0
for i in range(N):
  if S[i] == "a" and pass_student < AB:
    print("Yes")
    pass_student +=1
  elif S[i] =="b" and pass_student < AB and B_pass_student < B:
    print("Yes")
    pass_student += 1
    B_pass_student += 1
  else:
    print("No")
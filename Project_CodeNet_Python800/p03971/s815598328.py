from sys import stdin
N,A,B = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()
#print(N,A,B)
#print(S)
n=0 #予選通過者人数
n_f=0 #海外学生通過者人数
for i in S:
  if i == "a":
    if n < A+B:
      print("Yes")
      n+=1
    else:
      print("No")
    continue
    
  if i == "b":
    if n < A+B and n_f < B:
      print("Yes")
      n+=1
      n_f+=1
    else:
      print("No")
    continue
    
  if i =="c":
    print("No")